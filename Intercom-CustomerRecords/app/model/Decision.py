from enum import IntEnum


class Decision(IntEnum):
    """
    Enum Decision define final decision for a given customer.
    """
    UNKNOWN = 0

    INVITE = 1
    NOT_INVITED = 2
