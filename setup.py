from os.path import abspath, dirname, join

from setuptools import find_packages, setup

HERE = dirname(abspath(__file__))

README = open(join(HERE, 'README.md')).read()
CHANGES = open(join(HERE, 'CHANGES.md')).read()

REQUIRES = ['Flask>=1.0.2', 'WeasyPrint>=47']


setup(
    name="convert2pdf",
    version="0.0.1",
    description="A converter to pdf wsgi.",
    long_description=README + '\n\n' + CHANGES,
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Makina Corpus',
    author_email='python@makina-corpus.org',
    url='https://github.com/courtem/wsgi-convert2pdf',
    keywords='web flask webservice convert wsgi',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
)
