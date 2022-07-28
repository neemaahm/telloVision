#Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates
import DroneState
import TrackerState
from djitellopy import Tello
import time

g0_r = np.array([[2.6030], [-2.4606], [-1.6157]])
gxa_r = np.array([[0.3805], [-5.3250], [-1.5978]])

Tracker = TrackerState.TrackerState(g0_r, gxa_r)
print(Tracker.get_tracker_pos())
time.sleep(5)
print(Tracker.get_tracker_pos())


# Coords = Coordinates.Coordinates()
# Coords.init_global_mission_pad(1, np.array([[1], [1], [0]]))
# Coords.init_global_mission_pad(7, np.array([[2], [2], [0]]))

# drone_0_g = np.array([[1],[1],[0]])
# myDrone = DroneState.DroneState(drone_0_g)
# tello = Tello()

# myDrone.connect_drone(tello)

# p_g = np.array([[2.5], [2], [1]])

# # myDrone.move_xyz_relative(tello, Coords, 1, 1, 0)
# myDrone.move_xyz_global(tello, Coords, p_g)
# print(myDrone.drone_state)

# myDrone.drone_shutdown(tello)
