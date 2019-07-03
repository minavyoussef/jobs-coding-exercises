import unittest

from app.LocationAppParameters import LocationAppParameters
from app.controller.ExecutionControllerTypes import ExecutionControllerTypes
from app.model.Location import Location


class TestingBase(unittest.TestCase):
    HOME_LOCATION = Location.from_decimal(53.366942, -6.218848)
    INTERCOM_LOCATION = Location.from_decimal(53.339428, -6.257664)

    @classmethod
    def prepare_standard_app_params(cls,
                                    input_file='../../data/customers.txt',
                                    latitude=53.339428,
                                    longitude=-6.257664,
                                    search_radius=100.0,
                                    execution_type=ExecutionControllerTypes.SINGLE_THREADED,
                                    stop_on_failure=False):
        location_app_parameters = LocationAppParameters()
        if input_file is not None:
            location_app_parameters.input_file = input_file
        if latitude is not None:
            location_app_parameters.latitude = latitude
        if longitude is not None:
            location_app_parameters.longitude = longitude
        if search_radius is not None:
            location_app_parameters.search_radius = search_radius
        if execution_type is not None:
            location_app_parameters.execution_type = execution_type
        if stop_on_failure is not None:
            location_app_parameters.stop_on_failure = stop_on_failure
        return location_app_parameters
