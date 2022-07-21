
from djitellopy import Tello
import pygame
import controls
import myGUI

myGUI = myGUI.myGUI()
controls = controls.controls()

tello = Tello()
print("hello")
controls.connect_drone(tello)

print("Tello Battery: " + str(tello.get_battery()))
while controls.do_loop:
    pygame.event.pump()
    myGUI.doVideoFeed(tello)
    controls.take_inputs()
    controls.check_shutdown(tello)
    myGUI.drawRectangles(controls.stick_values)
    controls.move_tello(tello, 60, 90, 20)

    pygame.display.update()
    myGUI.clock.tick(60)
