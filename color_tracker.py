#Color tracking code written by Shaunak Mehta

import numpy as np
import cv2
import time
from imutils.video import VideoStream


vs = VideoStream(src=0).start()
# time.sleep(2.0)
while(True):
    frame = vs.read()
    img = cv2.flip(frame, 1)

    roi = (142, 19, 341, 461)

    # clone = frame.copy()
    # img = clone#[int(roi[1]):int(roi[1] + roi [3]), \
                #int(roi[0]):int(roi[0] + roi[2])]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hsv = image

    red_upper = np.array([5, 255, 255], np.uint8)
    red_lower = np.array([0, 100, 20], np.uint8)

    red = cv2.inRange(hsv, red_lower, red_upper)
    kernal = np.ones ((15, 15), "uint8")
    red = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernal)

    (contoursred, hierarchy) =cv2.findContours (red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contourred in enumerate (contoursred):
        area = cv2.contourArea (contourred) 
        if (area > 1):
            x, y, w, h = cv2.boundingRect (contourred)
            img = cv2.rectangle (img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

    if len(contoursred) > 0:
        # Find the biggest contour
        biggest_contour = max(contoursred, key=cv2.contourArea)

        # Find center of contour and draw filled circle
        moments = cv2.moments(biggest_contour)
        centre_of_contour = (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00']))
        cv2.circle(img, centre_of_contour, 2, (0, 0, 255), -1)
        # Save the center of contour so we draw line tracking it
        center_points1 = centre_of_contour
        r1 = center_points1[0]
        c1 = center_points1[1]
        y = r1
        x = c1
        # print(c1, r1)
        print("target_x={}, target_y={}".format(x,y))
    cv2.imshow('Image window', img)
    # cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vs.stop()