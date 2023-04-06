import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

# [html 코드 분석]
soup = BeautifulSoup(html_src, 'html.parser')
# print(type(soup))
# print("\n")
#
# print(soup.head)
# print("\n")
# print(soup.body)
# print("\n")

# print("title 태그 요소: ", soup.title)
# print("title 태그 이름: ", soup.title.name)
# print("title 태그 문자열: ", soup.title.string)
#
# first_img = soup.find(name='img')
# print(first_img)
# print("\n")

# [이미지 저장하기]
# target_img = soup.find(name='img', attrs={'alt':'Seoul Metro 2000 series train on Line 2'})
# print(target_img)
# target_img_src = target_img.get('src')
# print("\n")
#
# target_img_resp = requests.get('http:' + target_img_src)
# out_file_path = "./output/download_img.jpg"
#
# with open(out_file_path, 'wb') as out_file:
#     out_file.write(target_img_resp.content)
#     print("이미지 파일로 저장했습니다")

# [하이퍼링크 추출하기]
# links = soup.find_all("a")
# print("하이퍼링크의 개수: ", len(links))
# print("\n")
# print("첫 3개의 원소: ", links[:3])
# print("\n")
#
# wiki_links = soup.find_all(name="a", href=re.compile("/wiki/"), limit=3)
# print("/wiki/ 문자열이 포함된 하이퍼링크: ", wiki_links)
#
# external_links = soup.find_all(name="a", attrs={"class": "external text"}, limit=3)
# print("class 속성으로 추출한 하이퍼링크: ", external_links)

# [CSS Selector 활용]
