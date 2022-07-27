from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.go_xyz_speed(100, 0, 0, 20)
tello.go_xyz_speed(0, 100, 0, 20)
tello.go_xyz_speed(0, 0, 100, 20)

tello.land()