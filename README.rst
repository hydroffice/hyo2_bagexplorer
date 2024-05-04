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

BAG Explorer is a light application, based on HDF Compass and the HydrOffice BAG library tools, to explore BAG data files.

HDF Compass is written in Python, but ships as a native application on Windows, OS X, and Linux, by using PyInstaller and Py2App to package the app.
For more info about HDF Compass, visit the `GitHub <http://github.com/HDFGroup/hdf-compass>`_ repository and the `project <https://www.hdfgroup.org/projects/compass/>`_ web page.

HydrOffice BAG library provides access to BAG-specific features, as well as a collection of tools to verify and manipulate BAG data files.


Dependencies
------------

For executing and packaging the *BAG Explorer* app:

* ``hdf_compass`` (that requires several dependencies as ``matplotlib``, ``wxPython``, ``h5py``)
* ``hydroffice.bag`` (that also requires ``lxml`` and ``osgeo.gdal``)
* ``PyInstaller`` *[for freezing the application]*
* ``appdmg`` *[for creating a dmg on Mac]*
