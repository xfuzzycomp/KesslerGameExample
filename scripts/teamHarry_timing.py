import math
from typing import Tuple


def time_to_target(dx: Tuple[float, float], dv: Tuple[float, float]):

    vm = 800

    a = dv[0]**2 + dv[1]**2 - vm**2
    b = 2 * (dx[0]*dv[0] + dx[1]*dv[1])
    c = dx[0]**2 + dx[1]**2

    det = b*b - 4*a*c

    if det > 0:
        return 2*c / (math.sqrt(det) - b)
    else:
        return -1

