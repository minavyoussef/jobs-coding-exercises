from Services.Location.DistanceCalculatorKernel import DistanceCalculatorKernel
from Services.UnitsConversionService import UnitsConversionServices
from app.model.Location import Location
from common.Validator import Validator
from common.config import inject_default_config, Config


class LocationService:
    """
    Class LocationService represents a location service wrapper.
    """

    def __init__(self):
        self._reference_location = None

    def set_reference_location(self, reference_location):
        self._reference_location = reference_location

    def distance(self, target_location, config=inject_default_config()):
        Validator.is_type(target_location, Location)
        Validator.is_type(config, Config)

        # Calculate raw distance in metres.
        distance_in_metres = DistanceCalculatorKernel.distance_in_metres(self.reference_location, target_location)

        # Apply custom unit conversion, (if any).
        distance_in_target_unit = UnitsConversionServices.to(distance_in_metres, config.search_distance_unit)
        # Apply rounding.
        rounded_distance_in_metres = round(distance_in_target_unit, config.search_precision)

        return rounded_distance_in_metres

    @property
    def reference_location(self):
        return self._reference_location

    @reference_location.setter
    def reference_location(self, value):
        Validator.is_type(value, Location)

        self._reference_location = value
