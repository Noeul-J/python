# import datetime
#
#
# # 데코레이터 작성
# def datetime_decorator(func):
#     def wrapper():
#         print('time ' + str(datetime.datetime.now()))
#         func()
#         print(datetime.datetime.now())
#     return wrapper
#
#
# # 데코레이터 적용
# @datetime_decorator
# def logger_login_david():
#     print("David login")
#
#
# logger_login_david()

# [데코레이터 적용]
# def outer_func(function):
#     def inner_func():
#         print('decoration added')
#         function()
#     return inner_func
#
#
# @outer_func         # == decorated_func = outer_func(log_func); decorated_func()
# def log_func():
#     print('logging')
#
#
# log_func()


# # [인자가 있는 데코레이터]
# def outer_func(function):
#     def inner_func(digit1, digit2):
#         if digit2 == 0:
#             print('cannot be divided with zero')
#             return
#         function(digit1, digit2)
#     return inner_func
#
#
# def type_checker(function):
#     def inner_func(digit1, digit2):
#         if (type(digit1) != int) or (type(digit2) != int):
#             print('only integer support')
#             return
#         return function(digit1, digit2)
#     return inner_func
#
#
# @outer_func
# def divide(digit1, digit2):
#     print(digit1 / digit2)
#
#
# @type_checker
# def muliplexer(digit1, digit2):
#     return digit1 * digit2
#
#
# muliplexer(4, 2)
#
# # divide(4, 0)


# # [파라미터와 관계없이 모든 함수에 적용 가능한 데코레이터]
# def general_decorator(function):
#     def wrapper(*args, **kwargs):
#         print('function is decorated')
#         return function(*args, **kwargs)
#     return wrapper
#
#
# @general_decorator
# def calc_square(digit):
#     return digit * digit
#
#
# @general_decorator
# def calc_plus(digit1, digit2):
#     return digit1 + digit2
#
#
# @general_decorator
# def calc_quad(digit1, digit2, digit3, digit4):
#     return digit1 * digit2 * digit3 * digit4
#
#
# print(calc_square(2))
# print(calc_plus(2, 3))
# print(calc_quad(2, 3, 4, 5))

# # [한 함수에 여러 데코레이터 적용하기]
# # -- 데코레이터는 나열된 순서대로 적용됨
# def decorator1(function):
#     def wrapper():
#         print('decorator1')
#         function()
#     return wrapper
#
#
# def decorator2(function):
#     def wrapper():
#         print('decorator2')
#         function()
#     return wrapper
#
#
# @decorator1
# @decorator2
# def hello():
#     print("hello")
#
# hello()

# # 예제 - HTML 웹페이지 태그 붙이는 데코레이터
# def mark_bold(function):
#     def wrapper(*args, **kwargs):
#         return '<b>' + function(*args, **kwargs) + '</b>'
#     return wrapper
#
#
# def mark_italic(function):
#     def wrapper(*args, **kwargs):
#         return '<i>' + function(*args, **kwargs) + '</i>'
#     return wrapper
#
#
# @mark_bold
# @mark_italic
# def add_html(string):
#     return string
#
# print(add_html("안녕하세요"))

# # [Method Decorator]
# def h1_tag(function):
#     def func_wrapper(self, *args, **kwargs):    # self를 무조건 첫 파라미터로 넣어야 메서드에 적용가능
#         return "<h1>{0}</h1>".format(function(self, *args, **kwargs))   # function에도 self 넣어야함
#     return func_wrapper
#
#
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @h1_tag
#     def get_name(self):
#         return self.first_name + ' ' + self.last_name
#
#
# davelee = Person('Lee', 'Dave')
# print(davelee.get_name())

# # [파라미터가 있는 데코레이터 만들기]
# # -- 중첩 함수에 하나 더 깊게 두어 생성
# def decorator1(num):
#     def outer_wrapper(function):
#         def inner_wrapper(*args, **kwargs):
#             print('decoratr1 {}'.format(num))
#             return function(*args, **kwargs)
#         return inner_wrapper
#     return outer_wrapper
#
#
# @decorator1(1)        # print_hello2 = decorator1(1)(print_hello)
# # @decorator1(num=2) 로 써도 됨
# def print_hello():
#     print('hello')
#
#
# print_hello()

# 실습 - HTML 웹페이지 태그와 같이 태그 이름을 넣으면 HTML 문법에 맞게 출력해주는 데코레이터
def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return inner_wrapper
    return outer_wrapper


tag_list = ['b', 'i', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'center']


for t in tag_list:
    @mark_html(t)
    def print_hello(text):
        return text
    print(print_hello('태그 정하기 테스트 중'))
