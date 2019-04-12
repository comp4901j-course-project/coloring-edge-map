from six.moves.urllib import request
import zipfile
import os

url = "http://www.josiahwang.com/dataset/leedsbutterfly/leedsbutterfly_dataset_v1.0.zip"

file_name = url.split('/')[-1]
u = request.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.get("Content-Length"))
print("Downloading: %s Bytes: %s" % (file_name, file_size))

file_size_dl = 0
block_sz = 1048576 # 2 to the power of 20
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = "%d  [%3.2f%%]\r" % (file_size_dl, file_size_dl * 100. / file_size)
    print(status, end = "")

f.close()

print('Extracting: %s' % file_name)
t = zipfile.ZipFile(file_name, "r")  
t.extractall(path = '.')  
t.close()  
print('Removing: %s' % file_name)
os.remove(file_name)

