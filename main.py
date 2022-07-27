#Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates
import DroneState
from djitellopy import Tello

drone_0_g = np.array([[1],[1],[0]])
Coords = Coordinates.Coordinates(drone_0_g)
Coords.init_global_mission_pad(1, np.array([1], [1], [0]))
Coords.init_global_mission_pad(7, np.array([2], [2], [0]))

myDrone = DroneState.DroneState()
tello = Tello()

myDrone.connect_drone(tello)

myDrone.move_xyz(Coords, tello, 1, 1, 0)

print(myDrone.drone_state)

myDrone.drone_shutdown()
