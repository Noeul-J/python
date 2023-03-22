import pytest


# 함수 데코레이터를 생성
def test2(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper


# 데코레이터를 붙여 함수를 만든다
# @test2
def hello():
    print("hello")


# 함수를 호출
test_hello = test(hello)    # 데코레이터에 호출할 함수를 넣음
test_hello()
# hello()
