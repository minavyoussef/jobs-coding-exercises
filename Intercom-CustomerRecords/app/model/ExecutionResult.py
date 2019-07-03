from app.model.Decision import Decision
from common.Validator import Validator


class ExecutionResult:
    """
    class ExecutionResult represents execution level result.
    """

    def __init__(self, success=True, error='', data_records_list=[], report_decision_list=[Decision.INVITE]):
        self._success = success
        self._error = error
        self._data_records_list = data_records_list
        self._report_decision_list = report_decision_list

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        Validator.is_type(value, bool)
        self._success = value

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        Validator.is_type(value, str)
        self._error = value

    @property
    def data_records_list(self):
        return self._data_records_list

    @data_records_list.setter
    def data_records_list(self, value):
        Validator.is_type(value, list)
        self._data_records_list = value

    @property
    def report_decision_list(self):
        return self._report_decision_list

    @report_decision_list.setter
    def report_decision_list(self, value):
        Validator.is_type(value, list)
        self._report_decision_list = value
