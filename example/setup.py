#!/usr/bin/env python
import os
import sys

from setuptools import setup, find_packages


# Get current directory where setup is running
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

# Change directory
if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)


setup(
    name="Я-профессионал",
    version="0.0.1",
    description='Промоакции и розыгрыши призов',
    long_description='Вопрос №3. Промоакции и розыгрыши призов (максимум 40 баллов)',
    packages=find_packages(
        exclude=[]
    ),
    include_package_data=True,
    zip_safe=False,
)
