import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.like import Like  # noqa: E501
from openapi_server.models.play import Play  # noqa: E501
from openapi_server.models.track import Track  # noqa: E501
from openapi_server import util


def get_artist_plays(id_artist):  # noqa: E501
    """Obtener reproducciones por artista

    Devuelve las reproducciones asociadas a un artista. # noqa: E501

    :param id_artist: 
    :type id_artist: str

    :rtype: Union[List[Play], Tuple[List[Play], int], Tuple[List[Play], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_artist_top_tracks(id_artist):  # noqa: E501
    """Canciones más escuchadas por artista

    Devuelve las canciones más escuchadas de un artista. # noqa: E501

    :param id_artist: 
    :type id_artist: str

    :rtype: Union[List[Track], Tuple[List[Track], int], Tuple[List[Track], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recommended_tracks(id_user, type=None):  # noqa: E501
    """Consultar canciones recomendadas

    Devuelve canciones recomendadas para el usuario filtradas por like, género o suscripción. # noqa: E501

    :param id_user: 
    :type id_user: str
    :param type: 
    :type type: str

    :rtype: Union[List[Track], Tuple[List[Track], int], Tuple[List[Track], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_top_tracks():  # noqa: E501
    """Canciones más escuchadas

    Devuelve el listado de canciones más escuchadas. # noqa: E501


    :rtype: Union[List[Track], Tuple[List[Track], int], Tuple[List[Track], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_track_likes(id_track):  # noqa: E501
    """Obtener likes por canción

    Devuelve los likes de una canción. # noqa: E501

    :param id_track: 
    :type id_track: str

    :rtype: Union[List[Like], Tuple[List[Like], int], Tuple[List[Like], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_track_plays(id_track):  # noqa: E501
    """Obtener reproducciones por canción

    Devuelve las reproducciones de una canción. # noqa: E501

    :param id_track: 
    :type id_track: str

    :rtype: Union[List[Play], Tuple[List[Play], int], Tuple[List[Play], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_likes(id_user):  # noqa: E501
    """Obtener likes de usuario

    Devuelve los likes del usuario. # noqa: E501

    :param id_user: 
    :type id_user: str

    :rtype: Union[List[Like], Tuple[List[Like], int], Tuple[List[Like], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_plays(id_user):  # noqa: E501
    """Obtener reproducciones de usuario

    Devuelve las reproducciones del usuario. # noqa: E501

    :param id_user: 
    :type id_user: str

    :rtype: Union[List[Play], Tuple[List[Play], int], Tuple[List[Play], int, Dict[str, str]]
    """
    return 'do some magic!'
