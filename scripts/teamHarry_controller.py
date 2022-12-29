from typing import Tuple, Dict, Any

from kessler_game import KesslerController
from typing import Dict, Tuple

from teamHarry_aiming import aiming_function
import math
import numpy


class HarrysFuzzyController(KesslerController):
    @property
    def name(self) -> str:
        return "Harry Stamper's Crew"

    def __init__(self):
        self.aimValue = 0

    def actions(self, ship_state: Dict, game_state: Dict) -> Tuple[float, float, bool]:

        asteroidList = game_state["asteroids"]
        shipPosition = ship_state["position"]
        shipAngle = ship_state["heading"]
        asteroidNum = len(asteroidList)

        if asteroidNum:
            asteroidDist = []
            for ast in asteroidList:
                position = ast["position"]
                deltaX = position[0] - shipPosition[0]
                deltaY = position[1] - shipPosition[1]
                deltaNorm = abs(deltaX) + abs(deltaY)
                asteroidDist.append(deltaNorm)
            distMin = min(asteroidDist)
            distIdx = asteroidDist.index(distMin)

            activeAsteroid = asteroidList[distIdx]

            self.aimValue = aiming_function(activeAsteroid, ship_state)
            fire = False

            if self.aimValue:
                aimDelta = self.aimValue * 180 / 3.1415926 - (shipAngle)
                if aimDelta > 0:
                    turn_rate = 100
                    thrust = 0
                    if aimDelta < 10 * math.pi / 180:
                        fire = True
                elif aimDelta < 0:
                    turn_rate = -100
                    thrust = 0
                    if aimDelta > -10 * math.pi / 180:
                        fire = True
                else:
                    turn_rate = 0
                    thrust = 0
                    fire = False
            else:
                turn_rate = 0
                thrust = 0
                fire = False
            return thrust, turn_rate, fire









