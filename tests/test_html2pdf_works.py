from unittest import TestCase

from requests import post
from tests.settings import (EMPTY_HTML_PATH, ONE_PAGE_HTML_PATH,
                            TEN_PAGES_HTML_PATH)


class TestHtml2PdfWorks(TestCase):

    def test_empty_html_to_pdf(self):
        files = {'file': ('document.html', open(EMPTY_HTML_PATH, 'rb'),
                          'text/html')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 901)

    def test_one_page_html_to_pdf(self):
        files = {'file': ('document.html', open(ONE_PAGE_HTML_PATH, 'rb'),
                          'text/html')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 19468)

    def test_ten_pages_html_to_pdf(self):
        files = {'file': ('document.html', open(TEN_PAGES_HTML_PATH, 'rb'),
                          'text/html')}
        response = post('http://127.0.0.1:8000/', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content), 84782)
