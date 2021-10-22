import logging

from hyo2.abc.lib.logging import set_logging
from hyo2.bagexplorer import explorer

set_logging(ns_list=["hyo2.bag", "hyo2.bagexplorer"])

explorer.run()
