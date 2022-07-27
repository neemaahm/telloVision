# Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates

# This class handles controlling and retrieving state from a single Tello EDU drone
class DroneState:

    def __init__(self, initial_drone_pos = 0):
        if initial_drone_pos == 0:
            initial_drone_pos = np.array([[0],[0],[0]])
        self.drone_state = initial_drone_pos
        self.drone_history = initial_drone_pos
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
    def connect_drone(self, tello_drone):
        # Connect to Tello
        tello_drone.connect()
        tello_drone.streamoff()
        tello_drone.streamon()
        print("Tello Battery: " + str(tello_drone.get_battery()))

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
        if id == -1:
            return False
        else:
            m_x = tello_drone.get_mission_pad_distance_x()
            m_y = tello_drone.get_mission_pad_distance_y()
            m_z = tello_drone.get_mission_pad_distance_z()
            drone_m = np.array([[m_x], [m_y], [m_z]])
            self.drone_state = Coords.global_pos_drone(id, drone_m)
            self.drone_history = np.dstack((self.drone_history, self.drone_state))
            return True

    #moves the tello drone a certain amount in the x, y, and z direction relative to its current position
    def move_xyz(self, Coords, tello_drone, x, y, z, speed=20):
        tello_drone.go_xyz_speed(x, y, z, speed)
        if not self.read_pos(tello_drone, Coords):
            self.drone_state = np.array([[self.drone_state[0][0] + x],
                                         [self.drone_state[0][0] + y],
                                         [self.drone_state[0][0]] + z])
