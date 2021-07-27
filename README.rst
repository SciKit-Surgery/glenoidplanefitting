glenoidplanefitting
===============================

.. image:: https://github.com/astaolaf/glenoidplanefitting/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/astaolaf/glenoidplanefitting
   :alt: Logo

.. image:: https://github.com/astaolaf/glenoidplanefitting/badges/master/build.svg
   :target: https://github.com/astaolaf/glenoidplanefitting/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/astaolaf/glenoidplanefitting/badges/master/coverage.svg
    :target: https://github.com/astaolaf/glenoidplanefitting/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/glenoidplanefitting/badge/?version=latest
    :target: http://glenoidplanefitting.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Asta Olafsdottir

glenoidplanefitting is part of the `scikit-surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

glenoidplanefitting supports Python 2.7 and Python 3.6.

glenoidplanefitting is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python glenoidplanefitting.py 5 8
    python glenoidplanefitting.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/astaolaf/glenoidplanefitting


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc glenoidplanefitting


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/astaolaf/glenoidplanefitting



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2021 University College London.
glenoidplanefitting is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/astaolaf/glenoidplanefitting
.. _`Documentation`: https://glenoidplanefitting.readthedocs.io
.. _`scikit-surgery`: https://github.com/UCL/scikit-surgery/wiki
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/astaolaf/glenoidplanefitting/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/astaolaf/glenoidplanefitting/blob/master/LICENSE
