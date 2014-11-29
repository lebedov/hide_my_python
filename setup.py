#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from glob import glob

# Install setuptools if it isn't available:
try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from distutils.command.install import INSTALL_SCHEMES
from distutils.command.install_headers import install_headers
from setuptools import find_packages
from setuptools import setup

NAME =               'hide_my_python'
VERSION =            '0.1'
AUTHOR =             'Yannick Méheut'
AUTHOR_EMAIL =       'useless@utouch.fr'
URL =                'https://github.com/the-useless-one/hide_my_python'
MAINTAINER =         AUTHOR
MAINTAINER_EMAIL =   AUTHOR_EMAIL
DESCRIPTION =        'A parser for the free proxy list on HideMyAss!'
LONG_DESCRIPTION =   DESCRIPTION
DOWNLOAD_URL =       URL
LICENSE =            'GPLv3'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development']
NAMESPACE_PACKAGES = ['hmp']
PACKAGES =           find_packages()

if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    # This enables the installation of hmp/__init__.py as a data
    # file:
    for scheme in INSTALL_SCHEMES.values():
        scheme['data'] = scheme['purelib']

    setup(
        name = NAME,
        version = VERSION,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        classifiers = CLASSIFIERS,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        url = URL,
        maintainer = MAINTAINER,
        maintainer_email = MAINTAINER_EMAIL,
        namespace_packages = NAMESPACE_PACKAGES,
        packages = PACKAGES,
        package_data = {'hmp': ['countries_all']},
        scripts = ['hide_my_python.py'],
        
        # Force installation of __init__.py in namespace package:
        data_files = [('hmp', ['hmp/__init__.py'])],
        include_package_data = True,
        install_requires = [
            'requests',
        ],
        )
