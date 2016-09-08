#!/usr/bin/env python3

import os
import re
import subprocess as sp
import glob
import importlib

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGES = find_packages()
SERVICE_NAME = PACKAGES[0]


with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

with open(os.path.join(HERE, 'requirements.txt')) as f:
    REQUIREMENTS = [s.strip().replace('-', '_') for s in f.readlines()]


setup(name='{{cookiecutter.service_name.title()}} HTTP Service',
      version='1.0',
      description='{{cookiecutter.service_name.title()}} HTTP Service',
      long_description=README,
      author='Axial',
      author_email='daniel.gabriele@axial.net',
      install_requires=REQUIREMENTS,
      url=None,
      packages=PACKAGES,
      )
