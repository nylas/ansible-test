ansible-test: Ansible Local Testing Framework
=============================================

Ansible-test is a tool for testing your automation on local docker images. You can think of this as a slim version of Chef's test-kitchen

.. code-block:: bash

   $ cd /my/ansible/repository
   $ ansible-test my_ansible_role

The above command will drop a Dockerfile at the root of your ansible repo and initialize a docker image with ansible installed. It will then run the ansible role "my_ansible_role".

Note that ansible-test also accepts arbitrary arguments. These arguments will be passed onto the ansible-playbook command while running tests.

Installation
------------

To install ansible-test:

.. code-block:: bash

   $ pip install ansible-test

Documentation
-------------

ansible-test requires that you have docker installed locally. If you are using Mac OSX, I reccommend you use boot2docker.

NOTE: Given docker's inflexibility with Dockerfiles, ansible-test will overwrite the file Dockerfile at the current working directory from which you run ansible-test. This is currently the simplest way to integrate docker as a testing tool.
