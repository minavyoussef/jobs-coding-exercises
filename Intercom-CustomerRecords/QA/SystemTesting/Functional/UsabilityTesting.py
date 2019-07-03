import sys
from io import StringIO

from QA.TestingBase import TestingBase
from Services.DependencyInjection.InjectorKernal import init_injector
from app.LocationApp import LocationApp


class UsabilityTesting(TestingBase):
    """
    Class UsabilityTesting perform facade class testing of the whole app with different fault input combination.
    """

    def setUp(self):
        sys.stdout = StringIO()
        sys.stderr = StringIO()

        init_injector()

    def test_invalid_latitude(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.latitude = 'This is wrong'

    def test_invalid_longitude(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.longitude = 'This is wrong'

    def test_invalid_stop_on_failure(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.stop_on_failure = 'This is wrong'

    def test_invalid_search_radius(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.search_radius = 'This is wrong'

    def test_invalid_input_file(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.input_file = []

    def test_invalid_execution_type(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params()
            location_app_parameters.execution_type = 'This is wrong'

    def test_missing_latitude(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(latitude=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_longitude(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(latitude=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_stop_on_failure(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(stop_on_failure=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_search_radius(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(search_radius=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_input_file(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(input_file=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_execution_type(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(execution_type=None)
            location_app = LocationApp(location_app_parameters)
            location_app.run()