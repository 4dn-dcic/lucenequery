import os.path
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name='lucenequery',
    version='0.1',
    description='Parse queries in Lucene and Elasticsearch syntaxes',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=['lucenequery'],
    author='Laurence Rowe',
    author_email='laurence@lrowe.co.uk',
    url='http://github.com/lrowe/lucenequery',
    license='Apache',
    extras_require={
        ':python_version<"3.0"': ['antlr4-python2-runtime'],
        ':python_version>="3.0"': ['antlr4-python3-runtime'],
    },
)
