import cv2
from djitellopy import Tello

#Connect to Tello
tello = Tello()
tello.connect()
print("Tello Battery: " + str(tello.get_battery()))
tello.takeoff()
tello.land()

# tello.streamon()
# Running loop
# for i in range(100):
#
#     # Retrieve image from Tello
#     frame_read = tello.get_frame_read()
#     liveFrame = frame_read.frame
#     cv2.imshow("Tello Video Feed", liveFrame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
