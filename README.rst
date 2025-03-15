HydrOffice BAG Explorer
=======================

.. image:: https://github.com/hydroffice/hyo2_bagexplorer/raw/master/hyo2/bagexplorer/media/BAGExplorer_256.png
    :alt: logo

|

.. image:: https://img.shields.io/pypi/v/hyo2.bagexplorer.svg
    :target: https://pypi.python.org/pypi/hyo2.bagexplorer
    :alt: PyPi version

.. image:: https://github.com/hydroffice/hyo2_bagexplorer/actions/workflows/bagexplorer_on_windows.yml/badge.svg
    :target: https://github.com/hydroffice/hyo2_bagexplorer/actions/workflows/bagexplorer_on_windows.yml
    :alt: Windows

.. image:: https://github.com/hydroffice/hyo2_bagexplorer/actions/workflows/bagexplorer_on_linux.yml/badge.svg
    :target: https://github.com/hydroffice/hyo2_bagexplorer/actions/workflows/bagexplorer_on_linux.yml
    :alt: Linux

.. image:: https://app.codacy.com/project/badge/Grade/23c4dfc529ca446f88e5cd0cb8903d7f
    :target: https://app.codacy.com/gh/hydroffice/hyo2_bagexplorer/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
    :alt: codacy

.. image:: https://coveralls.io/repos/github/hydroffice/hyo2_bagexplorer/badge.svg?branch=master
    :target: https://coveralls.io/github/hydroffice/hyo2_bagexplorer?branch=master
    :alt: coverall

|

* Code: `GitHub repo <https://github.com/hydroffice/hyo2_bagexplorer <https://github.com/hydroffice/hyo2_bagexplorer>`_
* Project page: `url <https://www.hydroffice.org/bag/main>`_, `download <https://bitbucket.org/hydroffice/hyo2_bagexplorer/downloads/>`_
* License: LGPLv3 license (See `LICENSE <https://www.hydroffice.org/license/>`_)

|

General info
------------

HydrOffice is a research development environment for ocean mapping. It provides a collection of hydro-packages, each of them dealing with a specific issue of the field.
The main goal is to speed up both algorithms testing and research-2-operation.

BAG Explorer is a light application, based on `HDF Compass <http://github.com/HDFGroup/hdf-compass>`_ and the `HydrOffice BAG package <https://github.com/hydroffice/hyo2_bag>`_, to explore BAG data files.

   |info| **IMPORTANT NOTE**

   BAG is a data format developed and maintained by the `Open Navigation Surface Working Group <http://www.opennavsurf.org/>`_.

   For the official BAG reference implementation, go to `https://github.com/OpenNavigationSurface/BAG <https://github.com/OpenNavigationSurface/BAG>`_


.. |info| image:: https://www.hydroffice.org/img/info.svg
    :alt: info

Dependencies
------------

For executing and packaging the *BAG Explorer* app:

* ``hdf_compass`` (that requires several dependencies as ``matplotlib``, ``wxPython``, ``h5py``)
* ``hyo2.bag`` (that also requires ``lxml`` and ``osgeo.gdal``)
* ``hyo2.abc2``
* ``PyInstaller`` *[for freezing the application]*
* ``appdmg`` *[for creating a dmg on Mac]*
