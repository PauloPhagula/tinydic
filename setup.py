# coding: utf-8

from __future__ import unicode_literals, print_function
import os
import sys
import codecs
from email.utils import parseaddr
from setuptools import setup, find_packages

def file_get_contents(filename):
    """Reads an entire file into a string."""
    assert os.path.exists(filename) and os.path.isfile(filename), 'invalid filename: ' + filename
    return codecs.open(filename, 'r', 'utf-8').read()

SETUP_DIR = os.path.abspath(os.path.dirname(__file__))
LONG_DESCRIPTION = '\n'.join([file_get_contents('README.md')])

setup(
    name='TinyDIC',

    version='0.1.2',

    description='Tiny Python Dependency Injection Container.',
    long_description=LONG_DESCRIPTION,

    url='https://github.com/dareenzo/tinydic',

    author='Paulo Phagula',
    author_email='pphagula@gmail.com',

    license='See LICENSE',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
    ],

    keywords=('dic', 'ioc', 'dependency injection', 'inversion of control'),
    py_modules=['tinydic']
)
