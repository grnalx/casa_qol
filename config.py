import os
import time
if os.path.exists(os.getcwd()+'/casalogs') == False:
    os.mkdir(os.getcwd()+'/casalogs')
logfile = os.getcwd()+'/casalogs/casalog-%s.log' % time.strftime("%Y%m%d-%H%M%S", time.localtime())
