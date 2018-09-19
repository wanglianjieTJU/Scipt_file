import os
from datetime import datetime
def new_file(testdir):
    list = os.listdir(testdir)
    list.sort(key=lambda fn:os.path.getmtime(testdir+'\\'+fn))
    #filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir+list[-1]))
    filepath = os.path.join(testdir,list[-2])
    return filepath
print(new_file(u"G://"))
