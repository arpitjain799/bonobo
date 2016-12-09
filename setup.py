# This file is autogenerated by edgy.project code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages

tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))

def read(filename, flt=None):
    with open(filename) as f:
        content = f.read().strip()
        return flt(content) if callable(flt) else content

try:
    version = read('version.txt')
except:
    version = 'dev'

setup(
    name = 'bonobo',
    description = 'Bonobo',
    license = 'Apache License, Version 2.0',
    install_requires = [],
    version = version,
    long_description = read('README.rst'),
    classifiers = read('classifiers.txt', tolines),
    packages = find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data = True,
    extras_require = {'dev': ['coverage >=4.2,<4.3',
         'mock >=2.0,<2.1',
         'nose >=1.3,<1.4',
         'pylint >=1.6,<1.7',
         'pytest >=3,<4',
         'pytest-cov >=2.4,<2.5',
         'sphinx',
         'sphinx_rtd_theme']},
    url = 'https://github.com/hartym/bonobo',
    download_url = 'https://github.com/hartym/bonobo'.format(version=version),
)
