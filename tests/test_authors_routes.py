import json
from unittest import TestCase
from tests import client


class TestAuthors(TestCase):
    def test_get_authors_ok(self):
        response = client.get('/authors')

        assert response.status_code == 200

    def test_author_ok(self):
        author = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }

        createResponse = client.post(
            '/authors', data=json.dumps(dict(author=author)))
        createResult = json.loads(createResponse.data)

        assert createResponse.status_code == 200
        assert createResult['first_name'] == "First Name"
        assert createResult['last_name'] == "Last Name"

        getResponse = client.get('/authors/{}'.format(createResult['id']))
        getResult = json.loads(createResponse.data)

        assert getResponse.status_code == 200
        assert getResult['first_name'] == "First Name"
        assert getResult['last_name'] == "Last Name"

        newAuthor = {
            "first_name": "John",
            "last_name": "Doe",
        }

        updateResponse = client.put(
            '/authors/{}'.format(createResult['id']), data=json.dumps(dict(author=newAuthor)))
        updateResult = json.loads(updateResponse.data)

        assert updateResponse.status_code == 200
        assert updateResult['first_name'] == "John"
        assert updateResult['last_name'] == "Doe"

        deleteResponse = client.delete('/authors/{}'.format(getResult['id']))

        assert deleteResponse.status_code == 200

        getResponse = client.get('/authors/{}'.format(getResult['id']))

        assert getResponse.status_code == 404
