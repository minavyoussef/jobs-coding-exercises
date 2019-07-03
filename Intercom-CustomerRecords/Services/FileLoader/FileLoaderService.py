import os

import psutil

from Services.DependencyInjection.Injector import get_injector
from Services.DependencyInjection.InjectorModulesTypes import InjectorModulesTypes


class FileLoaderService:
    """
    Class FileLoaderService represents a strategy pattern for inner work of selected file loader.
    as file loader can either be InMemory or Stream file (if it is too big) or even other, and so
    it shield from actual used loader policy depending on available free memory
    """

    def __init__(self):
        self._file_loader = None

    def load(self, input_file):
        self.inject(input_file)
        self._file_loader.load(input_file)

    def read(self):
        return self._file_loader.read()

    def can_fit_in_memory(self, input_file):
        free_memory_in_mb = self.free_memory_in_mb()
        file_size_in_mb = self.file_size_in_mb(input_file)

        return file_size_in_mb < (free_memory_in_mb * .7)

    def inject(self, input_file):
        # If we can't fit the whole file in memory then we switch to stream file loader.

        injector = get_injector()
        if self.can_fit_in_memory(input_file):
            self._file_loader = injector.resolve(InjectorModulesTypes.IN_MEMORY_FILE_LOADER.value)
        else:
            self._file_loader = injector.resolve(InjectorModulesTypes.STREAM_FILE_LOADER.value)

    @staticmethod
    def free_memory_in_bytes():
        memory_info = psutil.virtual_memory()
        return memory_info.free

    @staticmethod
    def free_memory_in_mb():
        return FileLoaderService.free_memory_in_bytes() / 1024 / 1024

    @staticmethod
    def file_size_in_mb(file):
        if not os.path.isfile(file):
            return 0
        return os.stat(file).st_size / 1024 / 1024
