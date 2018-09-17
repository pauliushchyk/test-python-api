import json
from unittest import TestCase
from tests import client


class TestBooks(TestCase):
    def test_get_books_ok(self):
        response = client.get('/books')

        assert response.status_code == 200

    def test_book_ok(self):
        author = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }

        createAuthorResponse = client.post(
            '/authors', data=json.dumps(dict(author=author)))
        createAuthorResult = json.loads(createAuthorResponse.data)

        assert createAuthorResponse.status_code == 200

        book = {
            "name": "Name",
            "description": "Description",
            "pages": "123",
            "image": "",
            "author_id": createAuthorResult['id'],
            "genres": []
        }

        createResponse = client.post(
            '/books', data=json.dumps(dict(book=book)))
        createResult = json.loads(createResponse.data)

        assert createResponse.status_code == 200
        assert createResult['name'] == "Name"
        assert createResult['description'] == "Description"
        assert createResult['pages'] == 123

        getResponse = client.get('/books/{}'.format(createResult['id']))
        getResult = json.loads(createResponse.data)

        assert getResponse.status_code == 200
        assert getResult['name'] == "Name"
        assert getResult['description'] == "Description"
        assert int(getResult['pages']) == 123

        newBook = {
            "name": "Harry Potter",
            "description": "Description",
            "pages": "124",
            "image": "",
            "author_id": "1",
            "genres": []
        }

        updateResponse = client.put(
            '/books/{}'.format(createResult['id']), data=json.dumps(dict(book=newBook)))
        updateResult = json.loads(updateResponse.data)

        assert updateResponse.status_code == 200
        assert updateResult['name'] == "Harry Potter"
        assert updateResult['description'] == "Description"
        assert int(updateResult['pages']) == 124

        deleteResponse = client.delete('/books/{}'.format(getResult['id']))

        assert deleteResponse.status_code == 200

        getResponse = client.get('/books/{}'.format(getResult['id']))

        assert getResponse.status_code == 404

        deleteAuthorResponse = client.delete('/authors/{}'.format(createAuthorResult['id']))

        assert deleteAuthorResponse.status_code == 200
