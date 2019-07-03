from app.model.Decision import Decision
from common.Validator import Validator


class DataRecordResult:
    """
    Class DataRecordResult represents customer record result.
    """

    def __init__(self):
        self._decision = Decision.UNKNOWN
        self._distance_from_reference = 0

    def __repr__(self):
        return f"{{'decision':{self._decision.name}, 'distance_from_reference':{self._distance_from_reference}}}"

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        Validator.is_type(value, Decision)
        self._decision = value

    @property
    def distance_from_reference(self):
        return self._distance_from_reference

    @distance_from_reference.setter
    def distance_from_reference(self, value):
        Validator.is_type(value, float)
        self._distance_from_reference = value
