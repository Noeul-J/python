import requests

# url = 'https://www.python.org/'
# rep = requests.get(url)
# print(rep)                      # <Response [200]> '정상 응답'
#
# url2 = 'https://www.python.org/1'
# rep2 = requests.get(url2)
# print(rep2)                     # <Response [404]> '해당 페이지를 찾을 수 없다'
#
#
# html = rep.text
# print(html)                     # html 소스코드 출력

"""
로봇 배제 표준(robots.txt) - 웹 사이트에 로봇이 접근하는 것을 방지하기 위한 규약
User-agent: * Allow: /      - 모든 로봇에게 루트 디렉터리(/) 이하 모든 문서에 대한 접근을 허락
User-agent: * Disallow: /   - ""                                             차단
User-agent: * Disallow: /temp/ - 모든 로봇에게 특정 디렉터리(/temp/)에 대한 접근을 차단
User-agent: googlebot Disallow: /  - 특정 로봇에게 모든 문서에 대한 접근을 차단 
"""

url_list = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in url_list:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")
