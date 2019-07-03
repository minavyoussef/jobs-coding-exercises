import sys

from app.model.ExecutionResult import ExecutionResult
from common.PublisherSubscriber import Subscriber
from common.Validator import Validator


class ConsoleUserInterface(Subscriber):
    """
    Class ConsoleUserInterface represents the presentation layer, and act as subscriber to emitted published result
    """

    def notify(self, value):
        Validator.is_type(value, ExecutionResult)

        if value.success:
            self.print_result(value.data_records_list, value.report_decision_list)
        else:
            if not Validator.is_null_or_empty(value.error):
                self.print_error(value.error)

    def print_result(self, data_record_list, report_decision_list):
        data_record_list = sorted(data_record_list, key=lambda x: x.user_id)
        for data_record in data_record_list:
            if data_record.result.decision in report_decision_list:
                print(self.format_data_record(data_record))

    def format_data_record(self, data_record):
        return '%3s  %25s  %15s %5sKM' % (data_record.user_id,
                                          data_record.name,
                                          data_record.result.decision,
                                          data_record.result.distance_from_reference)

    def print_error(self, error_message):
        print(error_message, file=sys.stderr)
