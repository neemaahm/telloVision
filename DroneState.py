# Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates

# This class handles controlling and retrieving state from a single Tello EDU drone
class DroneState:

    def __init__(self, initial_drone_pos = np.array([[0.],[0.],[0.]])):
        self.drone_state = initial_drone_pos.astype(float)
        self.drone_history = initial_drone_pos.astype(float)
        self.fly_states = {True: "Flying", False: "Landed"}
        self.fly_state = False

    def get_drone_state(self):
        return self.drone_state

    # To read the output drone history: drone_history[coord][0][frame]
    # where coord is the coordinate of interest (x,y, or z)
    # and frame is the frame of interest (0 = initial frame, 4 = fifth frame)
    def get_drone_history(self):
        return self.drone_history

    # Connect Individual Tello Drone
    def connect_drone(self, tello_drone, takeoff=True):
        # Connect to Tello
        tello_drone.connect()
        print("Tello Battery: " + str(tello_drone.get_battery()))
        tello_drone.enable_mission_pads()
        tello_drone.set_mission_pad_detection_direction(2)
        if takeoff:
            tello_drone.takeoff()
            z_g = tello_drone.get_height()/100.
            self.drone_state[2][0] = z_g
            self.drone_history = np.dstack((self.drone_history, self.drone_state))

    # Shutdown Sequence
    def drone_shutdown(self, tello_drone):
        print("Shutdown Started")
        try:
            if self.fly_state:
                tello_drone.land()
        finally:
            self.fly_state = False
            print("Shutdown Completed")

    def read_pos(self, tello_drone, Coords):
        id = tello_drone.get_mission_pad_id()
        print(id)
        if id == -1:
            return False
        else:
            m_x = tello_drone.get_mission_pad_distance_x()/100
            m_y = tello_drone.get_mission_pad_distance_y()/100
            m_z = tello_drone.get_mission_pad_distance_z()/100
            print(m_x)
            print(m_y)
            print(m_z)
            drone_m = np.array([[m_x], [m_y], [m_z]])
            self.drone_state = Coords.global_drone_pos(id, drone_m)
            self.drone_history = np.dstack((self.drone_history, self.drone_state))
            return True

    # Moves the tello drone a certain amount in the x, y, and z direction relative to its current position
    # Input Units (x,y,z): meters
    def move_xyz_relative(self, tello_drone, Coords, x, y, z, speed=20):
        x_cm = int(x*100)
        y_cm = int(y*100)
        z_cm = int(z*100)
        tello_drone.go_xyz_speed(x_cm, y_cm, z_cm, speed)
        if not self.read_pos(tello_drone, Coords):
            self.drone_state = np.array([[self.drone_state[0][0] + x_cm/100.],
                                         [self.drone_state[1][0] + y_cm/100.],
                                         [self.drone_state[2][0] + z_cm/100.]])

    # Moves the tello drone to point p_g in the global reference frame
    #     p_g Input Format: np.array([[x], [y], [z]])       Units: meters
    def move_xyz_global(self, tello_drone, Coords, p_g, speed=20):
        # delta_g: delta between p_g and drone_g in the global frame (units: m)
        delta_g = Coords.global_pos_drone_relative(p_g, self.drone_state)
        x_cm = int(delta_g[0][0] * 100)
        y_cm = int(delta_g[1][0] * 100)
        z_cm = int(delta_g[2][0] * 100)
        tello_drone.go_xyz_speed(x_cm, y_cm, z_cm, speed)
        if not self.read_pos(tello_drone, Coords):
            self.drone_state = self.drone_state + delta_g

