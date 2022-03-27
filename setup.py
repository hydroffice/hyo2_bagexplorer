import codecs
import os
import re

from setuptools import setup, find_packages


# ------------------------------------------------------------------
#                         HELPER FUNCTIONS

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M, )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


# ------------------------------------------------------------------
#                          POPULATE SETUP

setup(
    name="hyo2.bagexplorer",
    version=find_version("hyo2", "bagexplorer", "__init__.py"),
    license="LGPLv3 license",

    namespace_packages=[
      "hyo2"
    ],
    packages=find_packages(exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests", "*.test*",
    ]),
    package_data={
        "": ["media/*.png", "media/*.ico", "media/*.icns", "media/*.txt",],
        'hyo2.bag': [
            'iso19139/bag/*',
            'iso19139/gco/*',
            'iso19139/gmd/*',
            'iso19139/gmi/*',
            'iso19139/gml/*.xsd',
            'iso19139/gml/*.txt',
            'iso19139/gml/3.1.1/smil/*',
            'iso19139/gsr/*',
            'iso19139/gss/*',
            'iso19139/gts/*',
            'iso19139/xlink/*',
            'iso19757-3/*',
            'samples/*',
        ],
    },
    zip_safe=False,
    setup_requires=[
        "setuptools",
        "wheel",
    ],
    install_requires=[
        "hdf_compass>=0.7b11",
        "hyo2.bag>=1.1.4"
    ],
    python_requires='>=3.5',
    entry_points={
        "gui_scripts": [
            'BAGExplorer = hyo2.bagexplorer.explorer:run',
        ],
        "console_scripts": [
        ],
    },
    test_suite="tests",

    description="An application to browse and manage BAG files.",
    long_description=(read('README.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +
                      read('HISTORY.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +
                      read('AUTHORS.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +
                      read(os.path.join('docs', 'how_to_contribute.rst')))
,
    url="https://www.hydroffice.org/bag",
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Office/Business :: Office Suites',
    ],
    keywords="hydrography ocean mapping survey bag tools",
    author="Giuseppe Masetti (CCOM,UNH)",
    author_email="gmasetti@ccom.unh.edu",
)
