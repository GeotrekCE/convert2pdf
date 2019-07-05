from unittest import TestCase

from requests import post
from tests.settings import (EMPTY_ODT_PATH, ONE_PAGE_ODT_PATH,
                            TEN_PAGES_ODT_PATH)


class TestOdt2PdfWorks(TestCase):

    def test_empty_odt_to_pdf(self):
        files = {'file': ('document.odt', open(EMPTY_ODT_PATH, 'rb'),
                          'application/vnd.oasis.opendocument.text')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 1143)

    def test_one_page_odt_to_pdf(self):
        files = {'file': ('document.odt', open(ONE_PAGE_ODT_PATH, 'rb'),
                          'application/vnd.oasis.opendocument.text')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 20890)

    def test_ten_pages_odt_to_pdf(self):
        files = {'file': ('document.odt', open(TEN_PAGES_ODT_PATH, 'rb'),
                          'application/vnd.oasis.opendocument.text')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 94332)
