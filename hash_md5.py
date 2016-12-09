import hashlib
from functools import partial

def md5(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)       
    s = d.hexdigest()
    drugi = 0
    for i in s:
        print(i.upper(), end = "")
        if drugi % 2 == 1 and drugi != len(s)-1:
            print("-", end="")
        drugi +=1

md5("hash_md5.py")
