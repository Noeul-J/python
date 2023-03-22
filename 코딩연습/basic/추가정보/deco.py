import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다")
        self.__radius = value


# 원의 둘레와 넓이 구하기
circle = Circle(10)

print("원의 반지름:", circle.radius)
circle.radius = 2
print("변경된 원의 반지름:", circle.radius)
print()

# 강제로 예외 발생
print("# 강제로 예외를 발생")
circle.radius = -10

"""
Traceback (most recent call last):
  File "C:\python\코딩연습\basic\추가정보\deco.py", line 34, in <module>
    circle.radius = -10
  File "C:\python\코딩연습\basic\추가정보\deco.py", line 20, in radius
    raise TypeError("길이는 양의 숫자여야 합니다")
TypeError: 길이는 양의 숫자여야 합니다
"""