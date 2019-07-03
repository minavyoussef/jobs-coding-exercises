import unittest

from Services.UnitsConversionService import UnitsConversionServices
from app.model.Units import DistanceUnit


class UnitsConversionServicesTester(unittest.TestCase):
    """
    Class UnitsConversionServicesTester defines unittest for unit conversion service wrapper.
    """

    def test_invalid_params(self):
        with self.assertRaises(TypeError):
            UnitsConversionServices.to(None, DistanceUnit.METRE)
        with self.assertRaises(TypeError):
            UnitsConversionServices.to(None, DistanceUnit.KILOMETRE)
        with self.assertRaises(TypeError):
            UnitsConversionServices.to('', DistanceUnit.METRE)
        with self.assertRaises(TypeError):
            UnitsConversionServices.to(1000.0, 0)

    def test_valid_conversion_to_km(self):
        self.assertEquals(UnitsConversionServices.to(1000.0, DistanceUnit.KILOMETRE), 1)

    def test_valid_conversion_to_m(self):
        self.assertEquals(UnitsConversionServices.to(1000.0, DistanceUnit.METRE), 1000.0)
