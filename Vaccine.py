# -*- coding:utf-8 -*-
import hashlib
import os

fp = open('./FilePiller.exe', 'rb')    
fbuf = fp.read()    
fp.close()

f = hashlib.md5()    # MD5 hash function
f.update(fbuf)    # hashing!
hashValue = f.hexdigest()    
print(hashValue)

if hashValue == '29990333db386c0dc9f9943c24b49b61':    # EICAR test 파일의 MD5 해시값
    print ("Warning! Malware was detected. Starting Delete...")
    os.remove('./FilePiller.exe')    
else:
    print ("Malware is not exist")
