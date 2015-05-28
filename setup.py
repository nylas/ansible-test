#!/usr/bin/env python

from setuptools import setup


setup(
    name='ansible_test',
    version='1.0',
    include_package_data = True,
    scripts=['bin/ansible-test'],
    install_requires=['Jinja2']
)
