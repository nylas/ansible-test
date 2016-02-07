#!/usr/bin/env python

from setuptools import setup


setup(
    name='ansible-test',
    version='1.0.1',
    description='An Ansible Testing Framework for Humans',
    url='https://github.com/nylas/ansible-test/',
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
