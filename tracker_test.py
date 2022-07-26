print("hello")
import triad_openvr
import time
import sys

v = triad_openvr.triad_openvr()
v.print_discovered_objects()
print("I made a triad object")
if len(sys.argv) == 1:
    print("I got to the first if")
    interval = 1/250
elif len(sys.argv) == 2:
    interval = 1/float(sys.argv[1])
    print("I got to the elif")
else:
    print("Invalid number of arguments")
    interval = False
    
if interval:
    while(True):
        start = time.time()
        txt = ""
        for each in v.devices["tracker_1"].get_pose_euler():
            txt += "%.4f" % each
            txt += " "
        print("\r" + txt, end="")
        sleep_time = interval-(time.time()-start)
        if sleep_time>0:
            time.sleep(sleep_time)
