How to release
==============

Versioning
----------

You need to install and run the `bumpversion`.

The above version value must agree with the variables ``version`` and ``release`` present in the ``conf.py`` under the `docs` folder.


PyInstaller
-----------

For the `BAGExplorer.1file.spec` file, you need to verify that the following parameters are passed to the ``EXE()`` function:

* ``console=False``: to avoid that a console window is opened at run-time for standard I/O
* ``debug=False``: to avoid that the boot-loader issues progress messages while initializing and starting the bundled app

