#!/usr/bin/env python

from os import path
from sys import version_info, exit
from setuptools import setup, find_packages

py_version = version_info[:2]
if py_version <= (3, 3):
    print('pwned requires Python version 3.3 or later, ' +
          '({}.{} detected).'.format(*py_version))
    exit(1)

here = path.abspath(path.dirname(__file__))
readme = path.join(here, 'README.md')

try:
    import pwned
except ImportError:
    print('Cannot access the pwned module, ' +
          'is the source tree broken?')

try:
    import pypandoc

    if path.exists(readme):
        long_description = pypandoc.convert(readme, 'rst')
    else:
        long_description = None
except ImportError:
    print('pypandoc is required for README conversion.')
    long_description = None

setup(
    name='pwned',
    version=pwned.__version__,
    description='Check if you\'ve been pwned via haveibeenpwned.com',
    long_description=long_description,
    url='https://github.com/SShrike/pwned',
    author='Severen Redwood',
    author_email='severen@shrike.me',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    keywords='password haveibeenpwned security',
    packages=find_packages(exclude=['script', 'tests']),
    install_requires=[
        'click',
        'requests',
    ],
    extras_require={
        'dev': ['twine'],
        'test': ['pytest'],
    },

    entry_points={'console_scripts': [
        'pwned = pwned.cli:pwned'
    ]}
)
