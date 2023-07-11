import urllib.request
import sys
import os


def img_down(down_url, down_path, down_file_name):
    try:
        file_path = os.path.join(down_path, down_file_name)
        urllib.request.urlretrieve(down_url, file_path)
        print(f"{file_path} -- 저장 완료")
        return file_path
    except Exception as e:
        print(f"Exception occurred:\n{e}")
        return "Error"


if __name__ == "__main__":
    url = sys.argv[1]
    path = sys.argv[2]
    file_name = sys.argv[3]

    result = img_down(url, path, file_name)

    print("<peon>")
    print(result)
    print("</peon>")
