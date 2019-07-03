import json
import logging

from Services.FileLoader.FileLoaderService import FileLoaderService
from Services.FileLoader.InMemoryFileLoader import InMemoryFileLoader
from Services.FileLoader.StreamFileLoader import StreamFileLoader
from Services.DependencyInjection.Injector import get_injector
from Services.DependencyInjection.InjectorModulesTypes import InjectorModulesTypes
from Services.Location.LocationService import LocationService
from app.controller.MultithreadExecutionController import MultithreadExecutionController
from app.controller.SingleThreadExecutionController import SingleThreadExecutionController
from app.view.ConsoleUserInterface import ConsoleUserInterface


def init_injector():
    """
    init_injector initialize DependencyInjection

    :return: initialized injector object
    :rtype: injector
    """

    injector = get_injector()

    injector.clear()

    # [Controllers] Execution managers.
    injector.register(InjectorModulesTypes.SINGLE_THREADED_EXECUTION_MANAGER.value, SingleThreadExecutionController)
    injector.register(InjectorModulesTypes.MULTI_THREADED_EXECUTION_MANAGER.value, MultithreadExecutionController)

    # [View].
    injector.register(InjectorModulesTypes.CONSOLE_USER_INTERFACE.value, ConsoleUserInterface)

    # [Services]
    #   Location Services
    injector.register(InjectorModulesTypes.LOCATION_SERVICE.value, LocationService)
    #   File Loaders
    injector.register(InjectorModulesTypes.FILE_LOADER_SERVICE.value, FileLoaderService)
    injector.register(InjectorModulesTypes.IN_MEMORY_FILE_LOADER.value, InMemoryFileLoader)
    injector.register(InjectorModulesTypes.STREAM_FILE_LOADER.value, StreamFileLoader)

    logging.info('DI kernel initialized ' + str(injector.get_registered.keys()))
