# Neema Ahmadian - Collab - July 2022

import triad_openvr
import numpy as np
import Coordinates

#This class handles retrieving state from an HTC Vive tracker in an arbitrary global coordinate frame
class TrackerState:

    # Argument Format: np.array([[x], [y], [z]])
    # g0_r: global origin; x,y,z given in the relative coordinate frame
    # gxa_r: any second point along the global x-axis; x, y, z given in the relative coordinate frame
    def __init__(self):
        self.Coords = Coordinates.Coordinates()
        self.track = triad_openvr.triad_openvr()

    def set_global_coords(self, g0_r, gxa_r):
        self.Coords.init_global_tracker(g0_r, gxa_r)

    #THIS FUNCTION IS UNFINISHED
    def auto_set_global_coords(self):
        input("Place the tracker at the global origin then press enter.")
        pose_r = self.track.devices["tracker_1"].get_pose_euler()
        tracker_pos_r = np.array([[pose_r[0]], [pose_r[2]], [pose_r[1]]])
        # g0_r =

    # This function returns the tracker position in the global coordinate frame
    # Output Format: np.array([[x],[y],[z]])
    def get_tracker_pos(self):
        pose_r = self.track.devices["tracker_1"].get_pose_euler()
        tracker_pos_r = np.array([[pose_r[0]], [pose_r[2]], [pose_r[1]]])
        tracker_pos_g = self.Coords.global_pos_tracker(tracker_pos_r)
        return tracker_pos_g

    # This function prints the tracker position for an infinite amount of time
    def show_running_pos(self):
        tracker_pos_g = self.get_tracker_pos()
        txt = "Global Values: "
        txt += "%.4f" % tracker_pos_g[0] + " "
        txt += "%.4f" % tracker_pos_g[1] + " "
        txt += "%.4f" % tracker_pos_g[2] + " "

        print("\r" + txt, end="")


