from app.model.Units import DistanceUnit


def inject_default_config():
    """
    inject_default_config function return default configuration

    :return: Default configuration instance
    :rtype: Config
    """
    return Config()


class Config:
    """
    Config class represents application level configurations
    """

    SEARCH_PRECISION_DEFAULT = 1
    """
    Search precision defines searching rounding level, where 1 => 0.#, 2 => 0.## ...etc
    """

    SEARCH_DISTANCE_UNITS = DistanceUnit.KILOMETRE
    """
    Search distance units defines application level unit to be used in distances calculation. 
    """

    def __init__(self, search_precision=SEARCH_PRECISION_DEFAULT,
                 search_distance_unit=SEARCH_DISTANCE_UNITS):
        self._search_precision = search_precision
        self._search_distance_unit = search_distance_unit

    @property
    def search_precision(self):
        return self._search_precision

    @property
    def search_distance_unit(self):
        return self._search_distance_unit
