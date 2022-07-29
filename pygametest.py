
import time
import pygame
pygame.init()
pygame.joystick.init()
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

for i in range(1000):
    time.sleep(0.5)
    # pygame.event.pump()
    pygame.event.get()
    a_button_value = gamepad.get_button(0)
    b_button_value = gamepad.get_button(1)
    if a_button_value == 1:
        print("A PRESS")
    if b_button_value == 1:
        print("B PRESS")
