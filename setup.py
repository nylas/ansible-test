#!/usr/bin/env python

from setuptools import setup


setup(
    name='ansible_test',
    version='1.0',
    include_package_data = True,
    packages = ['ansible_test'],
    package_data = {
        "ansible_test": [
            "resources/Dockerfile.j2",
            "resources/inventory.yml",
            "resources/playbook.yml"]
    },
    scripts=['bin/ansible-test'],
    install_requires=['Jinja2']
)
