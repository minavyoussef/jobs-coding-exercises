from math import sin, cos, atan, sqrt, radians

import math

from app.model.Location import Location
from common.Validator import Validator


class DistanceCalculatorKernel:
    """
    Class DistanceCalculatorKernel represents main calculator procedure for a distance between given two distances.
    """
    EARTH_RADIUS_IN_METRES = 6371 * 1000

    @classmethod
    def distance_in_metres(cls, first_location, second_location):
        Validator.is_type(first_location, Location)
        Validator.is_type(second_location, Location)

        phi_1, lambda_1 = first_location.as_radian()
        phi_2, lambda_2 = second_location.as_radian()

        delta_lambda = lambda_2 - lambda_1

        nominator = sqrt((cos(phi_2) * sin(delta_lambda)) ** 2 +
                         (cos(phi_1) * sin(phi_2) - sin(phi_1) * cos(phi_2) * cos(delta_lambda)) ** 2)
        denominator = sin(phi_2) * sin(phi_1) + cos(phi_1) * cos(phi_2) * cos(delta_lambda)
        delta_rho = atan(nominator / denominator)

        if delta_rho < 0:
            delta_rho += radians(180)
        return DistanceCalculatorKernel.EARTH_RADIUS_IN_METRES * delta_rho
