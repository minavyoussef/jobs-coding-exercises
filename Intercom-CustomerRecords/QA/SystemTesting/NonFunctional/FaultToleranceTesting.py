import sys
from io import StringIO

from QA.TestingBase import TestingBase
from Services.DependencyInjection.InjectorKernal import init_injector
from app.LocationApp import LocationApp


class FaultToleranceTesting(TestingBase):
    """
    Class FaultToleranceTesting represent testing for invalid and missing elements in the input files.
    """

    def setUp(self):
        sys.stdout = StringIO()
        sys.stderr = StringIO()

        init_injector()

    def test_invalid_input_file_lat(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/invalid_customers_lat.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_invalid_input_file_long(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/invalid_customers_long.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_invalid_input_file_name(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/invalid_customers_name.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_invalid_input_file_user_id(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/invalid_customers_user_id.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_input_file_lat(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/missing_customers_lat.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_input_file_long(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/missing_customers_long.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_input_file_name(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/missing_customers_name.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()

    def test_missing_input_file_user_id(self):
        with self.assertRaises(Exception):
            location_app_parameters = self.prepare_standard_app_params(
                input_file='../../data/missing_customers_user_id.txt',
                stop_on_failure=True)
            location_app = LocationApp(location_app_parameters)
            location_app.run()
