import os

import shutil as sh
import zipfile as zip

loc = 'C:/ProgramData'
locbname = os.listdir(loc)



def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def getfile_size(n, s = 1000000):
    dirsize = 0
    for root, dirs, files in os.walk(n):
        for fn in files:
            try:
                path = os.path.join(root, fn)
                size = os.stat(path).st_size
                dirsize += size
                if size > s:
                    data = path,size, convert_bytes(size)
                    f.write(str(data) + '\n')
            except Exception:
                pass
f = open('Massive files.txt','w')
getfile_size(loc,1000000)
f.close()



