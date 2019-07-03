import logging
from Services.DependencyInjection.Injector import get_injector
from Services.DependencyInjection.InjectorModulesTypes import InjectorModulesTypes


class LocationApp:
    """
    Class represents the facade class of the application.
    """
    def __init__(self, location_app_params):
        self._location_app_params = location_app_params
        self._location_app_params.validate()

    def run(self):
        injector = get_injector()

        execution_type = self._location_app_params.execution_type

        executor = injector.resolve(execution_type.name)
        logging.info(f'Executor injected {type(executor).__name__}')

        presenter = injector.resolve(InjectorModulesTypes.CONSOLE_USER_INTERFACE.value)
        logging.info(f'Presenter injected {type(presenter).__name__}')

        # Subscribe presenter for execution result
        executor.append_on_result_listener(presenter)

        return executor.execute(self._location_app_params)
