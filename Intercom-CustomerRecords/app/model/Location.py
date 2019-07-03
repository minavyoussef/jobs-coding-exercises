from math import radians

from common.Validator import Validator


class Location:
    """
    Class Location model a given location.
    """

    def __init__(self, latitude, longitude):
        Validator.is_type(latitude, float)
        Validator.is_type(longitude, float)

        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        return f"{{latitude:{self._latitude}, 'longitude' :{self._longitude}}}"

    @classmethod
    def from_decimal(cls, latitude_decimal, longitude_decimal):
        return cls(latitude_decimal, longitude_decimal)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        Validator.is_type(value, float)
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        Validator.is_type(value, float)
        self._longitude = value

    def as_radian(self):
        return radians(self._latitude), radians(self._longitude)
