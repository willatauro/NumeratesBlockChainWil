import hashlib
import json

def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    #return '-'.join([str(block[key]) for key in block])
    # json to convert to string
    return hash_string_256(json.dumps(block,sort_keys=True).encode())


