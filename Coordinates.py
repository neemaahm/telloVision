#Neema Ahmadian - Collab - July 2022

import numpy as np

class Coordinates:
    # Input format: np.array([x], [y], [z])
    # g0_r: global origin; x,y,z given in the relative coordinate frame
    # gxa_r: any second point along the global x-axis; x, y, z given in the relative coordinate frame
    def __init__(self, g0_r, gxa_r):
        x_delta_r = gxa_r[0] - g0_r[0]
        y_delta_r = gxa_r[1] - g0_r[1]
        slope = y_delta_r / x_delta_r
        phi = np.arctan(slope)

        if y_delta_r > 0 and x_delta_r > 0:
            theta = -phi
            print("Quadrant 1 - Theta(neg) = " + str(theta))
        elif y_delta_r > 0 and x_delta_r < 0:
            theta = -np.pi - phi
            print("Quadrant 2 - Theta(neg) = " + str(theta))
        elif y_delta_r < 0 and x_delta_r < 0:
            theta = np.pi - phi
            print("Quadrant 3 - Theta(pos) = " + str(theta))
        elif y_delta_r < 0 and x_delta_r > 0:
            theta = -phi
            print("Quadrant 4 - Theta(pos) = " + str(theta))

        cos_theta = np.cos(theta)[0]
        sin_theta = np.sin(theta)[0]
        rotation_matrix = np.array([[cos_theta, -sin_theta, 0.],
                                    [-sin_theta, -cos_theta, 0.],
                                    [0., 0., 1.]])
        translation_matrix = -np.matmul(rotation_matrix, g0_r)
        wide_matrix = np.hstack([rotation_matrix, translation_matrix])
        self.homog_matrix = np.vstack([wide_matrix, [0.0, 0.0, 0.0, 1.0]])

        g0_g = np.matmul(self.homog_matrix, np.vstack((g0_r, np.array([1]))))
        gxa_g = np.matmul(self.homog_matrix, np.vstack((gxa_r, np.array([1]))))


    # Input format: np.array([x], [y], [z])
    #     p_r: arbitrary point in the tracking area; x,y,z given in the relative coordinate frame
    # Output:
    #     p_g: p_r expressed in the global coordinate frame
    def global_pos(self, p_r):
        p_r = np.vstack((p_r, np.array([1])))
        p_g = np.matmul(self.homog_matrix, p_r)
        return np.delete(p_g, 3, 0)
