from Services.DependencyInjection.InjectorKernal import get_injector
from common.PublisherSubscriber import Publisher


class ExecutionControllerBase:
    """
    class ExecutionControllerBase represents base for all controllers types.
    """

    def __init__(self):
        self._injector = get_injector()
        self._result_publisher = Publisher()

    def execute(self, location_app_params):
        """
        Abstract method defines how controller would execute request

        :param location_app_params: application parameters
        :type location_app_params: LocationAppParameters
        :return: list of data record containing result
        :rtype: list(DataRecord)
        """
        raise NotImplementedError

    def append_on_result_listener(self, result_listener_subscriber):
        self._result_publisher.subscribe(result_listener_subscriber)
