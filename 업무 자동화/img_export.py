import base64
import sys


def encode_base_64(url):
    with open(url, 'rb') as img:
        print("ddd")
        encode_data = base64.b64encode(img.read())
        print(encode_data)
        return {'code' : 'fail', 'message' : encode_data}


if __name__ == '__main__':
    url = sys.argv[1]
    # url = "C:\\RPA\\GNTEST.png"
    result = encode_base_64(url)
    print("<peon>")
    print(result)
    print("</peon>")