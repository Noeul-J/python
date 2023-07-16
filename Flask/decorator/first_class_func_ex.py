# def outer_func(num):
#     # 중첩 함수에서 외부 함수의 변수에 접근 가능
#     def inner_func():
#         print(num)
#         return 'complex'
#
#     return inner_func
#
#
# fn = outer_func(10)     # first-class function
# print(fn())             # closure 호출
#
# """
# first-class function
# - 함수 자체를 변수에 저장 가능
# - 함수의 인자에 다른 함수를 인수로 전달 가능
# - 함수의 반환 값(return 값)으로 함수를 전달 가능
# - python 함수들은 First-class 함수로 사용 가능
# """


# def calc_square(digit):
#     return digit * digit
#
#
# def calc_plus(digit):
#     return digit + digit
#
#
# def calc_quad(digit):
#     return digit * digit * digit * digit
#
#
# def list_square(function, digit_list):
#     result = list()
#     for digit in digit_list:
#         result.append(function(digit))
#     print (result)
#
#
# num_list = [1, 2, 3, 4, 5]
# list_square(calc_square, num_list)
# list_square(calc_plus, num_list)
# list_square(calc_quad, num_list)

# def logger(msg):
#     message = msg
#
#     def msg_creator():
#         print("[HIGH LEVEL]: ", message)
#     return msg_creator
#
#
# log1 = logger('Dave Log-in')
# print(log1)         # <function logger.<locals>.msg_creator at 0x000001D48E05BDC0>
# print(log1())       # [HIGH LEVEL]:  Dave Log-in

# # [first-class 활용]
# def html_creator(tag):
#     def text_wrapper(msg):
#         print("<{0}>{1}</{0}>".format(tag, msg))
#     return text_wrapper
#
#
# h1_html_creator = html_creator('h1')
# print(h1_html_creator)
#
# h1_html_creator('H1 태그는 타이틀을 표시')
# p_html_creator = html_creator('p')
# p_html_creator('p 태그는 문단을 표시')

# def list_creator(text):
#     def text_wrapper(msg):
#         print(f"{text}{msg}")
#     return text_wrapper
#
#
# func1 = list_creator('-')
# func1("파이썬 test 중")

import requests
from bs4 import BeautifulSoup


def show_list(mark):
    def text_wrapper(msg):
        print(f"{mark}{msg}")
    return text_wrapper


show = show_list('*')

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

link_titles = soup.select('ul#hobby_course_list > li')
for link_title in link_titles:
    show(link_title.get_text())

# *(왕초보) - 클래스 소개
# *(왕초보) - 블로그 개발 필요한 준비물 준비하기
# *(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
# *(왕초보) - 초간단 페이지 만들어보기
# *(왕초보) - 이쁘게 테마 적용해보기
# *(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
# *(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기