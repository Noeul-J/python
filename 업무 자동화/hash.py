import hashlib
import sys

def get_hash(text):
    m = hashlib.sha256()
    m.update(text.encode('utf-8'))
    hash_val = m.hexdigest()[:8]
    print("결과 : " + hash_val)
    return hash_val

if __name__ == "__main__":
    text = sys.argv[0]
    result = get_hash(text)
    print('<peon>')
    print(result)
    print('</peon>')