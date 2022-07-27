import triad_openvr
import numpy as np
import Coordinates

g0_r = np.array([[2.6030], [-2.4606], [-1.6157]])
gxa_r = np.array([[0.3805], [-5.3250], [-1.5978]])

Coords = Coordinates.Coordinates()
Coords.init_global_tracker(g0_r, gxa_r)

v = triad_openvr.triad_openvr()

while(True):
    
    pose_r = v.devices["tracker_1"].get_pose_euler()
    tracker_pos_r = np.array([[pose_r[0]], [pose_r[2]], [pose_r[1]]])
    tracker_pos_g = Coords.global_pos_tracker(tracker_pos_r)
    txt_global = "Global Values: "
    txt_global += "%.4f" % tracker_pos_g[0] + " "
    txt_global += "%.4f" % tracker_pos_g[1] + " "
    txt_global += "%.4f" % tracker_pos_g[2] + " "

    print("\r" + txt_global, end="")

