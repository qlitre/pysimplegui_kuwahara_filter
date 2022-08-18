# Author: qlitre
# Copyright (c) 2022- qlitre
# Licence: MIT

from setuptools import setup

DESCRIPTION = 'pysimplegui_kuwahara_editor: Image Editor by pysimplegui using kuwahara filter.'
NAME = 'pysimplegui_kuwahara_editor'
AUTHOR = 'qlitre'
URL = 'https://github.com/qlitre/pysimplegui_kuwahara_filter'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.0.1'
PYTHON_REQUIRES = '>=3.6'
INSTALL_REQUIRES = [
    'cycler==0.11.0',
    'fonttools==4.35.0',
    'kiwisolver==1.4.4',
    'matplotlib==3.5.3'
    'numpy==1.23.2'
    'opencv-python==4.6.0.66'
    'packaging==21.3'
    'Pillow==9.2.0'
    'pyparsing==3.0.9'
    'PySimpleGUI==4.60.3'
    'python-dateutil==2.8.2'
    'six==1.16.0'
]
PACKAGES = [
    'pysimplegui_kuwahara_filter'
]
KEYWORDS = 'pysimplegui kuwahara filter'
CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    maintainer=AUTHOR,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)
