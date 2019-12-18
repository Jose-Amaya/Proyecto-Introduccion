import os
path = os.getcwd() + "\\2. Programación\\project\\data\\files\\" ## Informacion despacho nacional

import logging
loggingFile = open(path + 'dataUpdater.log','a')
logging.basicConfig(stream=loggingFile,level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("testing btich")