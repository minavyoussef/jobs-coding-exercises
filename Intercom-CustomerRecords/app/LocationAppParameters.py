from app.controller.ExecutionControllerTypes import ExecutionControllerTypes
from app.model.Location import Location
from common.Validator import Validator


class LocationAppParameters:
    """
    Class LocationAppParameters represents wrapper for all the parameters of LocationApp class.
    """
    def __init__(self):
        self._input_file = None
        self._execution_type = None
        self._latitude = None
        self._longitude = None
        self._search_radius = None
        self._stop_on_failure = None

    @classmethod
    def from_args(cls, args):
        location_app_params = LocationAppParameters()

        location_app_params.input_file = args.input_file
        location_app_params.latitude = args.latitude
        location_app_params.longitude = args.longitude
        location_app_params.search_radius = args.search_radius
        location_app_params.stop_on_failure = args.stop_on_failure

        # Execution type (Single | Multi) threaded
        if args.multithread_enable:
            location_app_params.execution_type = ExecutionControllerTypes.MULTI_THREADED
        else:
            location_app_params.execution_type = ExecutionControllerTypes.SINGLE_THREADED

        return location_app_params

    def validate(self):
        Validator.is_type(self.input_file, str)
        Validator.file_exists(self.input_file)
        Validator.is_type(self.execution_type, ExecutionControllerTypes)
        Validator.is_type(self.latitude, float)
        Validator.is_type(self.longitude, float)
        Validator.is_type(self.search_radius, float)
        Validator.is_type(self.stop_on_failure, bool)

    @property
    def input_file(self):
        return self._input_file

    @input_file.setter
    def input_file(self, value):
        Validator.file_exists(value)
        self._input_file = value

    @property
    def execution_type(self):
        return self._execution_type

    @execution_type.setter
    def execution_type(self, value):
        Validator.is_type(value, ExecutionControllerTypes)
        self._execution_type = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        Validator.is_type(value, float)
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        Validator.is_type(value, float)
        self._longitude = value

    @property
    def search_radius(self):
        return self._search_radius

    @search_radius.setter
    def search_radius(self, value):
        Validator.is_type(value, float)
        self._search_radius = value

    @property
    def stop_on_failure(self):
        return self._stop_on_failure

    @stop_on_failure.setter
    def stop_on_failure(self, value):
        Validator.is_type(value, bool)
        self._stop_on_failure = value

    def extract_location(self):
        return Location(self.latitude, self.longitude)
