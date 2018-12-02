import wx

import logging
log = logging.getLogger(__name__)

from hdf_compass.compass_viewer.viewer import load_plugins
from hdf_compass.compass_viewer import open_store, CompassApp
from hdf_compass import utils

from hyo2.bagexplorer import frame


class BagExplorerApp(CompassApp):
    def __init__(self, redirect):
        """ Constructor.  If *redirect*, show a windows with console output."""
        super(BagExplorerApp, self).__init__(redirect=redirect)
        self.SetAppName("BAG Explorer")


def run():
    """ Run BAG Explorer.  Handles all command-line arguments, etc."""

    try:
        import faulthandler
        faulthandler.enable()
    except ImportError:
        pass

    import sys
    import os.path as op

    app = BagExplorerApp(False)

    load_plugins()

    urls = sys.argv[1:]

    for url in urls:
        if "://" not in url:
            # assumed to be file path
            url = utils.path2url(op.abspath(url))
        if not open_store(url):
            log.warning('Failed to open "%s"; no handlers' % url)

    f = frame.InitFrame()

    if utils.is_darwin:
        wx.MenuBar.MacSetCommonMenuBar(f.GetMenuBar())
    else:
        f.Show()

    app.MainLoop()
