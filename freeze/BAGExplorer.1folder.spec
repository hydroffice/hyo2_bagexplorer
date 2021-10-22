# Builds a single-folder EXE for distribution.
# Note that an "unbundled" distribution launches much more quickly, but
# requires an installer program to distribute.
#
# To compile, execute the following within the source directory:
#
# python /path/to/pyinstaller.py freeze/BAGExplorer.1folder.spec
#
# The resulting .exe file is placed in the dist/BAGExplorer folder.
#
# REQUIRED TO MANUALLY COPY: wx\lib\pubsub\core or pubsub\sub
#
# Uploading to BitBucket: curl -s -v -u giumas:password -X POST https://api.bitbucket.org/2.0/repositories/hydroffice/hyo_bagexplorer/downloads -F files=@BAGExplorer.1.1.0.zip


from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE, TOC
from PyInstaller.compat import is_darwin
import os
import sys

from hyo2.bagexplorer import __version__ as bagexplorer_version

sys.setrecursionlimit(20000)


def collect_pkg_data(package, include_py_files=False, subdir=None):
    from PyInstaller.utils.hooks import get_package_paths, remove_prefix, PY_IGNORE_EXTENSIONS

    # Accept only strings as packages.
    if type(package) is not str:
        raise ValueError

    pkg_base, pkg_dir = get_package_paths(package)
    if subdir:
        pkg_dir = os.path.join(pkg_dir, subdir)
    # Walk through all file in the given package, looking for data files.
    data_toc = TOC()
    for dir_path, dir_names, files in os.walk(pkg_dir):
        for f in files:
            extension = os.path.splitext(f)[1]
            if include_py_files or (extension not in PY_IGNORE_EXTENSIONS):
                source_file = os.path.join(dir_path, f)
                dest_folder = remove_prefix(dir_path, os.path.dirname(pkg_base) + os.sep)
                dest_file = os.path.join(dest_folder, f)
                data_toc.append((dest_file, source_file, 'DATA'))

    return data_toc

pkg_data_bag = collect_pkg_data('hyo2.bag')
pkg_data_bagexplorer = collect_pkg_data('hyo2.bagexplorer')
pkg_data_hdf_compass = collect_pkg_data('hdf_compass')
cartopy_aux = []
try:  # for GeoArray we use cartopy that can be challenging to freeze on OSX to dependencies (i.e. geos)
    import cartopy.crs as ccrs
    cartopy_aux = collect_pkg_data('cartopy')
except (ImportError, OSError):
    pass

icon_file = os.path.normpath(os.path.join(os.getcwd(), 'freeze', 'BAGExplorer.ico'))
if is_darwin:
    icon_file = os.path.normpath(os.path.join(os.getcwd(), 'freeze', 'BAGExplorer.icns'))

a = Analysis(['BAGExplorer.py'],
             pathex=[],
             hiddenimports=['scipy.linalg.cython_blas', 'scipy.linalg.cython_lapack',
                            'wx.adv', 'wx.html', 'wx.xml', 'pubsub.pub',
                            'scipy.linalg', 'scipy.integrate', "scipy._lib.messagestream"],  # for cartopy
             excludes=["PySide", "PyQt4", "pandas", "IPython",
                       "FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter"],
             hookspath=None,
             runtime_hooks=None)

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='BAGExplorer.%s' % bagexplorer_version,
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon=icon_file)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               pkg_data_bag,
               pkg_data_bagexplorer,
               pkg_data_hdf_compass,
               cartopy_aux,
               strip=None,
               upx=True,
               name='BAGExplorer.%s' % bagexplorer_version)
if is_darwin:
    app = BUNDLE(coll,
                 name='BAGExplorer.app',
                 icon=icon_file,
                 bundle_identifier=None)
