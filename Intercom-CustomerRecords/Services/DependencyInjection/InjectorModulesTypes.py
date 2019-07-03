from enum import Enum


class InjectorModulesTypes(Enum):
    """
    Enum InjectorModulesTypes defines different modules types for DependencyInjection container.
    """
    CONSOLE_USER_INTERFACE = 'ConsoleUserInterface'

    SINGLE_THREADED_EXECUTION_MANAGER = 'SINGLE_THREADED'
    MULTI_THREADED_EXECUTION_MANAGER = 'MULTI_THREADED'

    FILE_LOADER_SERVICE = 'FileLoaderService'
    IN_MEMORY_FILE_LOADER = 'InMemoryFileLoader'
    STREAM_FILE_LOADER = 'StreamFileLoader'

    LOCATION_SERVICE = 'LocationService'
