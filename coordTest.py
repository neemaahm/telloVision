import math
import numpy as np

theta = 0

g0_r = np.array([[2.6030], [-2.4606], [-1.6157]])
gxa_r = np.array([[0.3805], [-5.3250], [-1.5978]])

x_delta_r = gxa_r[0] - g0_r[0]
y_delta_r = gxa_r[1] - g0_r[1]
slope = y_delta_r/x_delta_r
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

rotation_matrix = np.array([[np.cos(theta)[0], -np.sin(theta)[0], 0.],
                            [-np.sin(theta)[0], -np.cos(theta)[0], 0.],
                            [0., 0., 1.]])
translation_matrix = -np.matmul(rotation_matrix, g0_r)
wide_matrix = np.hstack([rotation_matrix, translation_matrix])
homog_matrix = np.vstack([wide_matrix, [0.0, 0.0, 0.0, 1.0]])

g0_g = np.matmul(homog_matrix, np.vstack((g0_r, np.array([1]))))
gxa_g = np.matmul(homog_matrix, np.vstack((gxa_r, np.array([1]))))

print(g0_g)
print(gxa_g)

# print("rotation: ", rotation_matrix)
# print("G0r: ", g0_r)
# print("translation: ", translation_matrix)
# print("homog: ", homog_matrix)