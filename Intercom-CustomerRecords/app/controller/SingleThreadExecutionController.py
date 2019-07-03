import logging

from Services.DependencyInjection.InjectorModulesTypes import InjectorModulesTypes
from app.controller.ExecutionControllerBase import ExecutionControllerBase
from app.model.DataRecord import DataRecord
from app.model.DataRecordResult import DataRecordResult
from app.model.Decision import Decision
from app.model.ExecutionResult import ExecutionResult
from app.model.Units import DistanceUnit
from common.config import Config


class SingleThreadExecutionController(ExecutionControllerBase):
    """
    Class SingleThreadExecutionController represent sequential controller style execution.
    """

    def __init__(self):
        super().__init__()

        self._custom_config = Config(search_distance_unit=DistanceUnit.KILOMETRE, search_precision=1)
        self._location_services = self._injector.resolve(InjectorModulesTypes.LOCATION_SERVICE.value);

    def execute(self, location_app_params):
        # Update location service with reference location to compute all distances from.
        self._location_services.set_reference_location(location_app_params.extract_location())

        # Get & prepare file loader
        file_loader_service = self._injector.resolve(InjectorModulesTypes.FILE_LOADER_SERVICE.value)
        file_loader_service.load(location_app_params.input_file)
        logging.info(f'File loader service injected {type(file_loader_service).__name__}')

        # Process customers entry-by-entry.
        result = []
        line_number = 1
        for entry in file_loader_service.read():
            try:
                process_entry = self.process(entry, location_app_params.search_radius)
                logging.info(f'Processing line number {line_number} result: ' + repr(process_entry.result))
                result.append(process_entry)
            except Exception as exception:
                error_message = f'Fail to process line {line_number} ' + repr(exception)
                logging.error(error_message)

                if location_app_params.stop_on_failure:
                    raise Exception(error_message)

                execution_result = ExecutionResult(success=False, error=error_message)
                self._result_publisher.notify(execution_result)

            line_number += 1

        execution_result = ExecutionResult(success=True, error='')
        execution_result.data_records_list = sorted(result, key=lambda x: x.user_id)
        execution_result.report_decision_list = [Decision.INVITE]  # Only report on invited customers.

        # Emit result to subscribed listeners
        self._result_publisher.notify(execution_result)
        return execution_result

    def process(self, entry, search_radius):
        data_record = DataRecord.from_json(entry)

        distance = self._location_services.distance(data_record, config=self._custom_config)

        result = DataRecordResult()
        result.decision = Decision.INVITE if distance <= search_radius else Decision.NOT_INVITED
        result.distance_from_reference = distance

        data_record.result = result
        return data_record
