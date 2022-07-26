import numpy as np
import Coordinates

g0_r = np.array([[2.6030], [-2.4606], [-1.6157]])
gxa_r = np.array([[0.3805], [-5.3250], [-1.5978]])

Coords = Coordinates.Coordinates(g0_r, gxa_r)

p_pos_g = np.array([[0.2305],[-2.6275],[-1.7106]])
print(Coords.global_pos(p_pos_g))

