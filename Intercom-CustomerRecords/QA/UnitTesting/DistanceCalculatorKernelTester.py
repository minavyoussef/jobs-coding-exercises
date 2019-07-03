import unittest

from Services.Location.DistanceCalculatorKernel import DistanceCalculatorKernel
from app.model.Location import Location


class DistanceCalculatorKernelTester(unittest.TestCase):
    """
    Class DistanceCalculatorKernelTester defines the testing functionality distance cal
    """

    HOME_LOCATION = Location.from_decimal(53.366942, -6.218848)
    INTERCOM_LOCATION = Location.from_decimal(53.339428, -6.257664)
    ANTIPODE_INTERCOM_LOCATION = Location.from_decimal(-53.339428, 173.742336)

    def test_invalid_params(self):
        location = Location.from_decimal(90.0, 180.0)
        with self.assertRaises(TypeError):
            DistanceCalculatorKernel.distance_in_metres(None, None)
        with self.assertRaises(TypeError):
            DistanceCalculatorKernel.distance_in_metres(None, location)
        with self.assertRaises(TypeError):
            DistanceCalculatorKernel.distance_in_metres(location, None)

    def test_valid_zero_distance(self):
        distance = DistanceCalculatorKernel.distance_in_metres(self.INTERCOM_LOCATION, self.INTERCOM_LOCATION)
        self.assertEquals(distance, 0)

    def test_valid_distance(self):
        distance = DistanceCalculatorKernel.distance_in_metres(self.HOME_LOCATION, self.INTERCOM_LOCATION)
        self.assertEquals(distance, 3999.618885656885)

    def test_valid_antipode_distance(self):
        distance = DistanceCalculatorKernel.distance_in_metres(self.ANTIPODE_INTERCOM_LOCATION, self.INTERCOM_LOCATION)
        self.assertEquals(distance, 20015086.79602057)

    def test_valid_distance_positive_positive(self):
        first_location = Location.from_decimal(35.6850, 139.7514)
        second_location = Location.from_decimal(35.707755, 139.763195)
        distance = DistanceCalculatorKernel.distance_in_metres(first_location, second_location)
        self.assertEquals(distance, 2745.291053330395)

    def test_valid_distance_positive_negative(self):
        first_location = Location.from_decimal(40.6943, -73.9249)
        second_location = Location.from_decimal(40.709964, -73.906146)
        distance = DistanceCalculatorKernel.distance_in_metres(first_location, second_location)
        self.assertEquals(distance, 2352.2417072468966)

    def test_valid_distance_negative_positive(self):
        first_location = Location.from_decimal(-26.185070, 28.040668)
        second_location = Location.from_decimal(-26.192176, 28.041351)
        distance = DistanceCalculatorKernel.distance_in_metres(first_location, second_location)
        self.assertEquals(distance, 793.0846456366976)

    def test_valid_distance_negative_negative(self):
        first_location = Location.from_decimal(-23.5587, -46.6250)
        second_location = Location.from_decimal(-23.568210, -46.626367)
        distance = DistanceCalculatorKernel.distance_in_metres(first_location, second_location)
        self.assertEquals(distance, 1066.6031054851721)
