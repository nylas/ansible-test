ansible-test: Ansible Local Testing Framework
=============================================

Ansible-test is a tool for testing your automation on local docker images. You can think of this as a slim version of Chef's test-kitchen.

.. code-block:: bash

   $ cd /my/ansible/repository
   $ ansible-test my_ansible_role

The above command will drop a Dockerfile at the root of your ansible repo and initialize a docker image with ansible installed. It will then run the ansible role "my_ansible_role".

Note that ansible-test also accepts arbitrary arguments. These arguments will be passed on to the ansible-playbook command while running tests:

.. code-block:: bash

   ansible-test my_ansible_role --ask-vault-pass


Ansible test also accepts an image argument to specify the base docker image:

.. code-block:: bash

   ansible-test my_ansible_role --image ubuntu:latest

See the `example ansible flask project <https://github.com/nylas/ansible-flask-example>`_, which tests with ansible-test out-of-the-box

Installation
------------

To install ansible-test:

.. code-block:: bash

   $ pip install ansible-test

Documentation
-------------

ansible-test requires that you have docker installed locally. If you are using Mac OSX, I recommend you use boot2docker.

NOTE: Given docker's inflexibility with Dockerfiles, ansible-test will overwrite the Dockerfile in the current working directory from which you run ansible-test. This is currently the simplest way to integrate docker as a testing tool.

Usage
~~~~~

.. code-block:: bash

   usage: ansible-test [-h] [--image IMAGE] [--family {Debian,RedHat,Gentoo}]
                       role

   positional arguments:
     role                  Role to test

   optional arguments:
     -h, --help            show this help message and exit
     --image IMAGE, -i IMAGE
                           Docker Base Image
     --family {Debian,RedHat,Gentoo}, -f {Debian,RedHat,Gentoo}
                           ansible_os_family value for Base Image
   
Tested image/family combinations:

| image *debian:7.7* / family *Debian*  <-- default values if not specified
| image *centos:centos7.2.1511* / family *RedHat*
| image *gentoo-amd64-plus-portage* / family *Gentoo*

Gentoo notes
------------

Rather than being able to simply pull official gentoo docker images, it was necessary to merge the stage3 and portage images to work around a docker limitation: docker currently has no way to mount volumes while building an image, only when starting up a container from an already-built image (see https://github.com/docker/docker/issues/3949 for further discussion of this limitation).

See `base-images/Dockerfile.gentoo-amd64-portage <base-images/Dockerfile.gentoo-amd64-portage>`_ as example for creating base image for testing on Gentoo. This Dockerfile inherits from `gentoo/stage3-amd64 Dockerfile <https://github.com/gentoo/gentoo-docker-images/blob/master/amd64/Dockerfile>`_ and adds the commands from `gentoo/portage Dockerfile <https://github.com/gentoo/gentoo-docker-images/blob/master/portage/Dockerfile>`_ in order to create a full stage3 image with /usr/portage included rather than relying on a separage image containing a portage volume. 
