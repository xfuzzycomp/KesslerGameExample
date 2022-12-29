import math
from teamHarry_timing import time_to_target


def aiming_function(asteroid, ship_state):

    shipPosition = ship_state["position"]
    shipVelocity = ship_state["velocity"]
    """
    astPosition = asteroid.position
    astVelocity = asteroid.velocity
    """

    astPosition = asteroid["position"]
    astVelocity = asteroid["velocity"]

    dx1 = astPosition[0] - shipPosition[0]
    dx2 = astPosition[1] - shipPosition[1]
    dv1 = astVelocity[0] - shipVelocity[0]
    dv2 = astVelocity[1] - shipVelocity[1]

    delta_position = (dx1, dx2)
    delta_velocity = (dv1, dv2)

    tf = time_to_target(delta_position, delta_velocity)

    if tf > 0:
        ap1 = astPosition[0] + dv1 * tf
        ap2 = astPosition[1] + dv2 * tf
        aimpoint = (ap1, ap2)

        dx1aim = aimpoint[0] - shipPosition[0]
        dx2aim = aimpoint[1] - shipPosition[1]

        deltaAngle = math.atan2(dx2aim, dx1aim)
    else:
        deltaAngle = False

    return deltaAngle

