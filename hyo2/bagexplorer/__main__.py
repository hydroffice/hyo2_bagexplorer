from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.logging import set_logging
from hyo2.bagexplorer import explorer

set_logging(ns_list=["hyo2.abc2", "hyo2.bag", "hyo2.bagexplorer", "hdf_compass"])
GdalAux.check_gdal_data()
explorer.run()
