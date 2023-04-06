import hashlib
import sys

def hash(text) :
    test = int.from_bytes(hashlib.sha256(b"H").digest()[:8], text)
    print(test)
    return test

if __name__ == "__main__" :
    text = sys.argv[1]
    result = hash(text)
    print('<peon>')
    print(result)
    print('</peon>')