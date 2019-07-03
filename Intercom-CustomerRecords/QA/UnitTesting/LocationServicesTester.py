import unittest

from Services.Location.LocationService import LocationService
from app.model.Location import Location
from app.model.Units import DistanceUnit
from common.config import Config


class LocationServicesTester(unittest.TestCase):
    """
    Class LocationServicesTester defines testing of distance calculator service wrapper.
    """

    HOME_LOCATION = Location.from_decimal(53.366942, -6.218848)
    INTERCOM_LOCATION = Location.from_decimal(53.339428, -6.257664)

    def test_invalid_params(self):
        with self.assertRaises(TypeError):
            LocationService(None)
        with self.assertRaises(TypeError):
            LocationService(0.0)
        with self.assertRaises(TypeError):
            LocationService('')

    def test_valid_zero_distance(self):
        location_services = LocationService()
        location_services.set_reference_location(LocationServicesTester.INTERCOM_LOCATION)
        distance = location_services.distance(LocationServicesTester.INTERCOM_LOCATION)
        self.assertEquals(distance, 0)

    def test_valid_distance_default_config(self):
        location_services = LocationService()
        location_services.set_reference_location(LocationServicesTester.INTERCOM_LOCATION)
        distance = location_services.distance(LocationServicesTester.HOME_LOCATION)
        self.assertEquals(distance, 4.0)

    def test_valid_distance_custom_config_unit(self):
        custom_config = Config(search_distance_unit=DistanceUnit.METRE)
        location_services = LocationService()
        location_services.set_reference_location(LocationServicesTester.INTERCOM_LOCATION)
        distance = location_services.distance(LocationServicesTester.HOME_LOCATION, config=custom_config)
        self.assertEquals(distance, 3999.6)

    def test_valid_distance_custom_config_all(self):
        custom_config = Config(search_precision=5, search_distance_unit=DistanceUnit.METRE)
        location_services = LocationService()
        location_services.set_reference_location(LocationServicesTester.INTERCOM_LOCATION)
        distance = location_services.distance(LocationServicesTester.HOME_LOCATION, config=custom_config)
        self.assertEquals(distance, 3999.61889)
