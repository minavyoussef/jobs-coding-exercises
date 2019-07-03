import json

from app.model.DataRecordResult import DataRecordResult
from app.model.Location import Location
from common.Validator import Validator


class DataRecord(Location):
    """
    Class DataRecord represents a given customer data record.
    """

    def __init__(self, latitude, longitude, user_id, name):
        super().__init__(latitude, longitude)

        self._user_id = user_id
        self._name = name
        self._result = None

    def __repr__(self):
        return f"{{'latitude':{self._latitude}, " \
               f"'longitude' :{self._longitude}, " \
               f"'user_id':{self.user_id}, " \
               f"'name':'{self.name}'" \
               f"'result':'{repr(self._result)}'}}"

    @classmethod
    def validate(cls, instance, member, expected_type):
        Validator.has(instance, member)
        value = expected_type(instance[member])
        Validator.is_type(value, expected_type)
        return value

    @classmethod
    def from_json(cls, raw_entry):
        record_json = json.loads(raw_entry)

        longitude = cls.validate(record_json, 'longitude', float)
        latitude = cls.validate(record_json, 'latitude', float)
        user_id = cls.validate(record_json, 'user_id', int)
        name = cls.validate(record_json, 'name', str)

        return cls(latitude, longitude, user_id, name)

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        Validator.is_type(value, int)
        self._user_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Validator.is_type(value, str)
        self._name = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        Validator.is_type(value, DataRecordResult)
        self._result = value
