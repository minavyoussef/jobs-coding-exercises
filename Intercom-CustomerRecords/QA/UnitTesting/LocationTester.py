import math
import unittest

from app.model.Location import Location


class LocationTester(unittest.TestCase):
    """
    Class LocationTester defines unittest for location class.
    """

    def test_invalid_none(self):
        with self.assertRaises(TypeError):
            Location.from_decimal(None, None)
        with self.assertRaises(TypeError):
            Location.from_decimal(0.0, None)
        with self.assertRaises(TypeError):
            Location.from_decimal(None, 1.1)

    def test_invalid_not_float(self):
        with self.assertRaises(TypeError):
            Location.from_decimal('', 0.0)
        with self.assertRaises(TypeError):
            Location.from_decimal(1, 0.0)
        with self.assertRaises(TypeError):
            Location.from_decimal(True, 0.0)

    def test_valid_location(self):
        location = Location.from_decimal(90.0, 180.0)
        self.assertEquals(location.latitude, 90.0)
        self.assertEquals(location.longitude, 180.0)

    def test_valid_long(self):
        location = Location.from_decimal(90.0, 180.0)
        location.longitude = 270.0
        self.assertEquals(location.longitude, 270.0)

    def test_valid_lat(self):
        location = Location.from_decimal(90.0, 180.0)
        location.longitude = 270.0
        self.assertEquals(location.longitude, 270.0)

    def test_valid_radian(self):
        location = Location.from_decimal(90.0, 180.0)
        long_rad, lat_rad = location.as_radian()
        self.assertEquals(long_rad, 90.0 * math.pi / 180.0)
        self.assertEquals(lat_rad, 180.0 * math.pi / 180.0)

    def test_invalid_valid_radian(self):
        location = Location.from_decimal(90.0, 180.0)
        long_rad, lat_rad = location.as_radian()
        self.assertNotEquals(long_rad, 180.0 * math.pi / 180.0)
        self.assertNotEquals(lat_rad, 90.0 * math.pi / 180.0)
