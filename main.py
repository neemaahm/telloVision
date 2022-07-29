#Neema Ahmadian - Collab - July 2022

import numpy as np
import Coordinates
import DroneState
import TrackerState
from djitellopy import Tello
import time
from threading import Thread
import pygame

# g0_r = np.array([[2.6030], [-2.4606], [-1.6157]])
# gxa_r = np.array([[0.3805], [-5.3250], [-1.5978]])

# Tracker = TrackerState.TrackerState(g0_r, gxa_r)
# print(Tracker.get_tracker_pos())
# time.sleep(5)
# print(Tracker.get_tracker_pos())


# Coords = Coordinates.Coordinates()
# Coords.init_global_mission_pad(1, np.array([[1], [1], [0]]))
# Coords.init_global_mission_pad(7, np.array([[2], [2], [0]]))



# p1_g = np.array([[2], [2], [1]])

# print("starting movement")
# tello.go_xyz_speed(-100, 0, 0, 50)
# tello.hover()

# print("stopped")

# myDrone.drone_shutdown(tello)

drone_0_g = np.array([[0],[0],[0]])
myDrone = DroneState.DroneState(drone_0_g)
tello = Tello()

myDrone.connect_drone(tello)


def droneThread():
    # print("Thread Start")
    tello.go_xyz_speed(300, 0, 0, 20)
    # print("Thread End")

recorder = Thread(target=droneThread)
# print("Before Thread")
recorder.start()
# print("After Thread")

def droneThread2():
    tello.go_xyz_speed(0, 100, 0, 20)
    
recorder2 = Thread(target=droneThread2)


pygame.init()
pygame.joystick.init()
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

while True:
    time.sleep(0.5)
    # pygame.event.pump()
    pygame.event.get()
    a_button_value = gamepad.get_button(0)
    b_button_value = gamepad.get_button(1)
    if a_button_value == 1:
        print("A PRESS")
        tello.hover()
        recorder.join()
        time.sleep(1)
        print("B PRESS")
        recorder2.start()


recorder2.join()

