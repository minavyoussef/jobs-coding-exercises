from app.model.Units import DistanceUnit
from common.Validator import Validator


class UnitsConversionServices:
    """
    Class UnitsConversionServices represents unit conversion service.
    """

    MAPPER = {
        DistanceUnit.METRE: lambda v: v,
        DistanceUnit.KILOMETRE: lambda v: v / 1000.0,
    }

    @classmethod
    def to(cls, metres, target_unit):
        Validator.is_type(metres, float)
        Validator.is_type(target_unit, DistanceUnit)

        if target_unit not in cls.MAPPER.keys():
            raise NotImplemented(f'Target unit {target_unit} not supported')

        return cls.MAPPER[target_unit](metres)
