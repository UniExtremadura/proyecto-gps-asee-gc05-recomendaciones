# openapi_server/models/rating.py

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401
from openapi_server.models.base_model import Model
from openapi_server import util

class Rating(Model):
    """
    Clase completa para el objeto Rating (Valoraciones).
    """

    def __init__(self, id=None, user_id=None, track_id=None, score=None, timestamp=None):  # noqa: E501
        """Rating - a model defined in OpenAPI

        :param id: The id of this Rating.  # noqa: E501
        :type id: str
        :param user_id: The user_id of this Rating.  # noqa: E501
        :type user_id: str
        :param track_id: The track_id of this Rating.  # noqa: E501
        :type track_id: str
        :param score: The score of this Rating (1-5).  # noqa: E501
        :type score: int
        :param timestamp: The timestamp of this Rating.  # noqa: E501
        :type timestamp: str
        """
        self.openapi_types = {
            'id': str,
            'user_id': str,
            'track_id': str,
            'score': int,
            'timestamp': str
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'track_id': 'track_id',
            'score': 'score',
            'timestamp': 'timestamp'
        }

        self._id = id
        self._user_id = user_id
        self._track_id = track_id
        self._score = score
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Rating':
        """Returns the dict as a model"""
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    @property
    def track_id(self) -> str:
        return self._track_id

    @track_id.setter
    def track_id(self, track_id: str):
        self._track_id = track_id

    @property
    def score(self) -> int:
        """Gets the score (1-5)."""
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self._timestamp = timestamp