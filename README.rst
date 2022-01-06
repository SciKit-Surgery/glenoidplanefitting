glenoidplanefitting
===============================

.. image:: https://github.com/SciKit-Surgery/glenoidplanefitting/raw/master/skglenoid_logo.png
   :height: 128px
   :width: 128px
   :target: https://github.com/SciKit-Surgery/glenoidplanefitting
   :alt: Logo


|

.. image:: https://github.com/SciKit-Surgery/glenoidplanefitting/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/SciKit-Surgery/glenoidplanefitting/actions
   :alt: GitLab-CI test status

.. image:: https://coveralls.io/repos/github/SciKit-Surgery/glenoidplanefitting/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/SciKit-Surgery/glenoidplanefitting?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/glenoidplanefitting/badge/?version=latest
    :target: http://glenoidplanefitting.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Cite-SciKit--Surgery-informational
   :target: https://doi.org/10.1007/s11548-020-02180-5
   :alt: The SciKit-Surgery paper

.. image:: https://img.shields.io/badge/-SciKit%20Surgery-blueviolet?style=flat&logo=youtube
   :target: https://youtu.be/0z8eIjqAbzQ
   :alt: SciKit-Surgery on YouTube

.. image:: https://img.shields.io/twitter/url?style=social&url=http%3A%2F%2Fscikit-surgery.org
   :target: https://twitter.com/intent/tweet?screen_name=scikit_surgery&ref_src=twsrc%5Etfw
   :alt: Get in touch via twitter

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter

.. image:: https://img.shields.io/badge/-See%20us%20at%20SPIE%20202-yellow?style=flat
   :target: https://spie.org/conferences-and-exhibitions/medical-imaging/program
   :alt: SPIE Medical Imaging 2022

Authors: Asta Olafsdottir, Stephen Thompson

glenoidplanefitting provides tools for measuring the Glenoid version, useful when 
planning reconstructive shoulder surgery.
glenoidplanefitting is part of the `scikit-surgery`_ software project, 
developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, 
part of `University College London (UCL)`_, in collaboration with surgeons at the 
Royal National Orthopaedic Hospital 

glenoidplanefitting is tested on Python 3.x, but may work with other versions of Python

glenoidplanefitting currently requires the user to manually identify relevant anatomical 
landmarks on the scapula and glenoid dish. These points can then be passed to 
glenoidplanefitting to calculate the Glenoid version using multiple methods. Example usage:

::

    python glenoidplanefitting.py --fried_points landmark_friedman.fcsv --output friedman.vtp --visualise glenoid.vtp

glenoidplanefitting is a work in progress with plans to automate the point picking to create
software to enable a large scale comparison of different methods of Glenoid version 
methods on a clinical data set. If you are interested in contributing to this work
please get in touch or follow the guides below.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/SciKit-Surgery/glenoidplanefitting


Running tests
^^^^^^^^^^^^^
We use tox to run tests and run static code analysis using Lint. 
::

    pip install tox
    python -m tox


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/SciKit-Surgery/glenoidplanefitting



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
.. _`source code repository`: https://github.com/SciKit-Surgery/glenoidplanefitting
.. _`Documentation`: https://glenoidplanefitting.readthedocs.io
.. _`scikit-surgery`: http://scikit-surgery.github.io/scikit-surgery/
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/glenoidplanefitting/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/glenoidplanefitting/blob/master/LICENSE

