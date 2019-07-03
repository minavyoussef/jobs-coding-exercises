from enum import IntEnum


class DistanceUnit(IntEnum):
    """
    Enum DistanceUnit defines supported distance units.
    """
    METRE = 1
    KILOMETRE = 2

    # TODO: Support of different units, for instance empirical system
