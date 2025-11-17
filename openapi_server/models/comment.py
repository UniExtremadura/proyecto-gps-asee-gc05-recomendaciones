# openapi_server/models/comment.py

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401
from openapi_server.models.base_model import Model
from openapi_server import util

class Comment(Model):
    """
    Clase completa para el objeto Comment.
    Incluye el campo 'status' para manejar la moderación (pending, approved, rejected).
    """

    def __init__(self, id=None, user_id=None, track_id=None, content=None, status='pending', timestamp=None):  # noqa: E501
        """Comment - a model defined in OpenAPI

        :param id: The id of this Comment.  # noqa: E501
        :type id: str
        :param user_id: The user_id of this Comment.  # noqa: E501
        :type user_id: str
        :param track_id: The track_id of this Comment.  # noqa: E501
        :type track_id: str
        :param content: The content of this Comment.  # noqa: E501
        :type content: str
        :param status: The status of this Comment (pending, approved, rejected).  # noqa: E501
        :type status: str
        :param timestamp: The timestamp of this Comment.  # noqa: E501
        :type timestamp: str
        """
        self.openapi_types = {
            'id': str,
            'user_id': str,
            'track_id': str,
            'content': str,
            'status': str,
            'timestamp': str
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'track_id': 'track_id',
            'content': 'content',
            'status': 'status',
            'timestamp': 'timestamp'
        }

        self._id = id
        self._user_id = user_id
        self._track_id = track_id
        self._content = content
        self._status = status
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The comment of this Comment.  # noqa: E501
        :rtype: Comment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Comment."""
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Comment."""
        self._id = id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Comment."""
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Comment."""
        self._user_id = user_id

    @property
    def track_id(self) -> str:
        """Gets the track_id of this Comment."""
        return self._track_id

    @track_id.setter
    def track_id(self, track_id: str):
        """Sets the track_id of this Comment."""
        self._track_id = track_id

    @property
    def content(self) -> str:
        """Gets the content of this Comment."""
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this Comment."""
        self._content = content

    @property
    def status(self) -> str:
        """Gets the status of this Comment."""
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Comment (e.g., 'pending', 'approved')."""
        self._status = status

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this Comment."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this Comment."""
        self._timestamp = timestamp