import unittest

from flask import json

from openapi_server.models.like import Like  # noqa: E501
from openapi_server.models.play import Play  # noqa: E501
from openapi_server.models.track import Track  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRecommendationsController(BaseTestCase):
    """RecommendationsController integration test stubs"""

    def test_get_artist_plays(self):
        """Test case for get_artist_plays

        Obtener reproducciones por artista
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/metrics/artists/{id_artist}/plays'.format(id_artist='id_artist_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_artist_top_tracks(self):
        """Test case for get_artist_top_tracks

        Canciones más escuchadas por artista
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/recommendations/artists/{id_artist}/top-tracks'.format(id_artist='id_artist_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recommended_tracks(self):
        """Test case for get_recommended_tracks

        Consultar canciones recomendadas
        """
        query_string = [('type', 'type_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/recommendations/users/{id_user}/recommended-tracks'.format(id_user='id_user_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_top_tracks(self):
        """Test case for get_top_tracks

        Canciones más escuchadas
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/recommendations/tracks/top',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_track_likes(self):
        """Test case for get_track_likes

        Obtener likes por canción
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/metrics/tracks/{id_track}/likes'.format(id_track='id_track_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_track_plays(self):
        """Test case for get_track_plays

        Obtener reproducciones por canción
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/metrics/tracks/{id_track}/plays'.format(id_track='id_track_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_likes(self):
        """Test case for get_user_likes

        Obtener likes de usuario
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/metrics/users/{id_user}/likes'.format(id_user='id_user_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_plays(self):
        """Test case for get_user_plays

        Obtener reproducciones de usuario
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/metrics/users/{id_user}/plays'.format(id_user='id_user_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
