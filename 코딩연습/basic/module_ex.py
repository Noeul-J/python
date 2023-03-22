# # math 모듈
# import math as m                 # from math import *
#
# print(m.sin(30))
# print(m.cos(30))
# print(m.tan(30))
# print(m.floor(2.5))              # 내림
# print(m.ceil(2.5))               # 올림
#
# # 정수부분이 짝수일 때 소수부분이 5라면 내리고, 홀수일때는 올려라
# print(round(2.5))                   # 2
# print(round(3.5))                   # 4


# # random 모듈
# import random
#
# # random(): 0.0 <= x < 1.0 사이의 float를 리턴
# print(" - random():", random.random())
#
# # uniform(min, max) : 지정한 범위 사이의 float를 리턴
# print(" - uniform(10, 20):", random.uniform(10, 20))
#
# # randrange() : 지정한 범위의 int를 리턴
# # - randrange(max) : 0부터 max 사이의 값을 리턴
# # - randrange(min, max) : min 부터 max 사이의 값을 리턴
# print(" - randrange(10):", random.randrange(10))
#
# # choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택
# print(" - choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))
#
# # shuffle(list) : 리스트의 요소들을 랜덤하게 섞는다
# print(" - shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
#
# # sample(list, k=<숫자>) : 리스트의 요소 중에 k개를 뽑는다
# print(" - sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))
#
#
# # sys 모듈
# import sys
#
# # 명령 매개변수를 출력
# print(sys.argv)
# print("---")
#
# # 컴퓨터 환경과 관련된 정보를 출력
# print("getwindowsversion:()", sys.getwindowsversion())
# print("---")
# print("copyright:", sys.copyright)
# print("---")
# print("version:", sys.version)
#
# # 프로그램 강제 종료
# sys.exit()


# # OS 모듈
# import os
#
# print("현재 운영체제:", os.name)
# print("현재 폴더:", os.getcwd())
# print("현재 폴더 내부의 요소:", os.listdir())
#
# # 폴더 생성 및 제거
# os.mkdir("hello")
# os.rmdir("hello")
#
# # 파일을 생성하고 + 파일 이름을 변경
# with open("original.txt", "w") as file:
#     file.write("hello")
# os.rename("original.txt", "new.txt")
#
# # 파일 제거
# os.remove("new.txt")
# # os.unlink("new.txt")
#
# # 시스템 명령어 실행
# os.system("dir")

# # datetime 모듈
# import datetime
#
# now = datetime.datetime.now()
# output_a = now.strftime("%Y-%m-%d %H:%M:%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
# output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")      # 문자열, 리스트 앞에 *를 붙이면 요소 하나하나가 매개변수로 지정됨
#
# print(output_a)
# print(output_b)
# print(output_c)
# print()
#
# # 특정 시간 이후의 시간 구하기
# after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
# print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# print()
#
# # 특정 시간 요소 교체
# output = now.replace(year=(now.year + 1))
# print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# # time 모듈
# import time
#
# print("지금부터 5초 동안 정지합니다!")
# time.sleep(5)
# print("프로그램을 종료합니다")

# # urlib 모듈
# from urllib import request
#
# # urlopen() 함수로 구글의 메인 페이지를 읽는다
# target = request.urlopen("https://google.com")
# output = target.read()
#
# print(output)

# # BeautifulSoup 모듈로 날씨 가져오기
# from urllib import request
# from bs4 import BeautifulSoup
#
# # 기상청의 전국 날씨를 읽습니다
# target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=100")
#
# # 웹페이지 분석
# soup = BeautifulSoup(target, "html.parser")
#
# # location 태그를 찾는다
# for location in soup.select("location"):
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

# # flask 모듈
# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "<h1>Hello World!</h1>"
