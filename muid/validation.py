from muid.corpus import search
from muid.crypto import bhash

def animal(key):
    bkey = key if isinstance(key,bytes) else key.encode('ascii')
    code = bhash(bkey)
    return search(code)

def validate(key):
   return animal(key) is not None



