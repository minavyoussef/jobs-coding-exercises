import errno
import os
import sys
from io import StringIO

from QA.TestingBase import TestingBase
from Services.FileLoader.FileLoaderService import FileLoaderService
from Services.DependencyInjection.InjectorKernal import init_injector
from app.LocationApp import LocationApp
from common.Validator import Validator


class StressTesting(TestingBase):
    """
    Class StressTesting present testing an extreamly large input file and see if application
    would handle it without crash and/or expcetion of any kind.
    """
    MAX_FILE_SIZE_IN_MB = 50

    def setUp(self):
        sys.stdout = StringIO()
        sys.stderr = StringIO()

        init_injector()

        self._temp_large_file = None
        self.generate_large_customer_files_by_size('../../data/customers.txt', StressTesting.MAX_FILE_SIZE_IN_MB)

    def tearDown(self):
        super().tearDown()
        self.cleanup()

    def test_stress(self):
        try:
            location_app_parameters = self.prepare_standard_app_params(input_file=self._temp_large_file)
            location_app = LocationApp(location_app_parameters)
            location_app.run()
        except Exception as exception:
            self.fail('Stress Testing failed exception occurred ' + repr(exception))

    def generate_large_customer_files_by_size(self, original_file, upper_limit_in_mb):
        self._temp_large_file = original_file + '.tmp~'
        with open(original_file, 'r') as infile:
            lines = infile.readlines()

            while FileLoaderService.file_size_in_mb(self._temp_large_file) < upper_limit_in_mb:
                append_write = 'a' if os.path.exists(self._temp_large_file) else 'w'
                with open(self._temp_large_file, append_write) as outfile:
                    outfile.writelines(lines)
                    outfile.write('\n')

        return self._temp_large_file

    def cleanup(self):
        if not Validator.is_null_or_empty(self._temp_large_file):
            try:
                os.remove(self._temp_large_file)
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise
