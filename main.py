#Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates
import DroneState
from djitellopy import Tello

Coords = Coordinates.Coordinates()
DroneState = DroneState.DroneState()
tello = Tello()

DroneState.connect_drone(tello)

