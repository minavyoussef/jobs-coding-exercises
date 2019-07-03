import json
import sys
from io import StringIO

from QA.TestingBase import TestingBase
from Services.DependencyInjection.InjectorKernal import init_injector
from app.LocationApp import LocationApp
from app.model.Decision import Decision


class SmokeTesting(TestingBase):
    """
    Class SmokeTesting perform standard use case testing given in requirement and compare with
    golden standard that was manually validated.
    """

    def setUp(self):
        sys.stdout = StringIO()
        sys.stderr = StringIO()

        init_injector()

    def test_standard_file(self):
        location_app_parameters = self.prepare_standard_app_params()
        location_app = LocationApp(location_app_parameters)

        data_records_list = location_app.run().data_records_list
        result = [repr(e) for e in data_records_list if e.result.decision == Decision.INVITE]

        with open('../../data/customers.result.json') as infile:
            expected = json.load(infile)

        self.assertEquals(result, expected)
