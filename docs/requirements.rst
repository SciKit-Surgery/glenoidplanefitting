.. highlight:: shell

.. _requirements:

===============================================
Requirements for glenoidplanefitting
===============================================

This is the software requirements file for glenoidplanefitting, part of the
SNAPPY project. The requirements listed below should define
what glenoidplanefitting does. Each requirement can be matched to a unit test that
checks whether the requirement is met.

Requirements
~~~~~~~~~~~~
+------------+--------------------------------------------------------+-------------------------------------+
|    ID      |  Description                                           |  Test                               |
+============+========================================================+=====================================+
|    0000    |  Module has a help page                                |  pylint, see                        |
|            |                                                        |  tests/pylint.rc and tox.ini        |
+------------+--------------------------------------------------------+-------------------------------------+
|    0001    |  Functions are documented                              |  pylint, see                        |
|            |                                                        |  tests/pylint.rc and tox.ini        |
+------------+--------------------------------------------------------+-------------------------------------+
|    0002    |  Package has a version number                          |  No test yet, handled by git.       |
+------------+--------------------------------------------------------+-------------------------------------+
|    0003    |  Provides a function to fit a plane to a list of      |                                     |
|            |  3 dimensional points                                  |                                     |
+------------+--------------------------------------------------------+-------------------------------------+
|    0004    |  Provides a command line application                   |                                     |
+------------+--------------------------------------------------------+-------------------------------------+
|    0005    |  What else ??                                          |                                     |
+------------+--------------------------------------------------------+-------------------------------------+




