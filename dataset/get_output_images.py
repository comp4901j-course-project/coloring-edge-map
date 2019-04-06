import os
from shutil import copyfile

cwd = os.getcwd()
path = cwd + "/output/"
src = cwd + "/BSR/BSDS500/data/images/"
dst = cwd + "/output/"
states = ["train/", "val/", "test/"]
    
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)
    
for state in states:
    for filename in sorted(os.listdir(src + state)):
        if filename.endswith(".jpg"):
            copyfile(src + state + filename, dst + filename)
        else:
            continue

