from os.path import dirname, join, realpath

ROOT = dirname(dirname(realpath(__file__)))
DOC_PATH = join(ROOT, 'tests', 'doc')
ODT_DOCS_PATH = join(DOC_PATH, 'odt')
HTML_DOCS_PATH = join(DOC_PATH, 'html')

EMPTY_ODT_PATH = join(ODT_DOCS_PATH, 'empty.odt')
ONE_PAGE_ODT_PATH = join(ODT_DOCS_PATH, 'one_page.odt')
TEN_PAGES_ODT_PATH = join(ODT_DOCS_PATH, 'ten_pages.odt')

EMPTY_HTML_PATH = join(HTML_DOCS_PATH, 'empty.html')
ONE_PAGE_HTML_PATH = join(HTML_DOCS_PATH, 'one_page.html')
TEN_PAGES_HTML_PATH = join(HTML_DOCS_PATH, 'ten_pages.html')
