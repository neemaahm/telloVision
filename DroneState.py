# Neema Ahmadian - Collab - July 2022

import numpy as np
import djitellopy

# This class handles controlling and retrieving state from a single Tello EDU drone
class DroneState:

    def __init__(self, initial_drone_pos = np.array([[0],[0],[0]])):
        self.drone_state = initial_drone_pos
        self.drone_history = initial_drone_pos
        self.fly_states = {True: "Flying", False: "Landed"}
        self.fly_state = False

    def get_drone_state(self):
        return self.drone_state

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

    #moves the tello drone a certain amount in the x, y, and z direction relative to its current position
    def move_xyz(self, tello_drone, x, y, z):
        tello_drone.

