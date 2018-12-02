HydrOffice BAG Explorer
=======================

.. image:: https://www.hydroffice.org/static/mybag/img/logo.png
    :alt: logo

* Code: `GitHub repo <https://github.com/hydroffice/hyo_bagexplorer <https://github.com/hydroffice/hyo_bagexplorer>`_
* Project page: `url <https://www.hydroffice.org/bag/main>`_
* Download page: `url <https://bitbucket.org/hydroffice/hyo_bagexplorer/downloads/>`_
* License: LGPLv3 license (See `LICENSE <https://www.hydroffice.org/license/>`_)    

General info
------------

.. image:: https://img.shields.io/pypi/v/hyo2.bagexplorer.svg
    :target: https://badge.fury.io/py/hyo2.bagexplorer
    :alt: PyPI Status

.. image:: https://ci.appveyor.com/api/projects/status/0pd1horwjasgjvkw?svg=true
    :target: https://ci.appveyor.com/project/giumas/hyo-bagexplorer
    :alt: AppVeyor Status

.. image:: https://travis-ci.org/hydroffice/hyo_bagexplorer.svg?branch=master
    :target: https://travis-ci.org/hydroffice/hyo_bagexplorer
    :alt: Travis-CI Status

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


Freezing
--------

Use of Pyinstaller
~~~~~~~~~~~~~~~~~~

* ``pyinstaller --clean -y freeze/BAGExplorer.1file.spec``
* ``pyinstaller --clean -y freeze/BAGExplorer.1folder.spec``

Creation of MAC OS dmg
~~~~~~~~~~~~~~~~~~~~~~

* ``appdmg spec.json dist/BAGExplorer.dmg``
