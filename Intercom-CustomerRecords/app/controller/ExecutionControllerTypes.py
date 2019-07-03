from enum import IntEnum


class ExecutionControllerTypes(IntEnum):
    """
    Enum ExecutionControllerTypes defines different type of execution controllers
    """
    SINGLE_THREADED = 1
    MULTI_THREADED = 2
