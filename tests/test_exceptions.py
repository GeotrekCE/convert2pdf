from io import BytesIO
from unittest import TestCase

from requests import post


class TestExceptions(TestCase):

    def test_bad_route(self):
        files = {}
        response = post('http://127.0.0.1:8000/bad/route', files=files)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, b'{"errors":["Bad url."]}\n')

    def test_bad_files_param(self):
        files = {}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"errors":["No file."]}\n')

    def test_bad_mime_type(self):
        files = {'file': ('doc.txt', BytesIO(b''), 'text/plain')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content,
            b'{"errors":["Invalid mime type: text/plain is not supported."]}\n')
