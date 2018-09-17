import json
from unittest import TestCase
from tests import client


class TestGenres(TestCase):
    def test_get_genres_ok(self):
        response = client.get('/genres')

        assert response.status_code == 200

    def test_genre_ok(self):
        genre = {
            "name": "Name",
        }

        createResponse = client.post(
            '/genres', data=json.dumps(dict(genre=genre)))
        createResult = json.loads(createResponse.data)

        assert createResponse.status_code == 200
        assert createResult['name'] == "Name"

        getResponse = client.get('/genres/{}'.format(createResult['id']))
        getResult = json.loads(createResponse.data)

        assert getResponse.status_code == 200
        assert getResult['name'] == "Name"

        newGenre = {
            "name": "Comedy",
        }

        updateResponse = client.put(
            '/genres/{}'.format(createResult['id']), data=json.dumps(dict(genre=newGenre)))
        updateResult = json.loads(updateResponse.data)

        assert updateResponse.status_code == 200
        assert updateResult['name'] == "Comedy"

        deleteResponse = client.delete('/genres/{}'.format(getResult['id']))

        assert deleteResponse.status_code == 200

        getResponse = client.get('/genres/{}'.format(getResult['id']))

        assert getResponse.status_code == 404
