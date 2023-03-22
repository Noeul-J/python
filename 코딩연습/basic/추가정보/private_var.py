import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value


# 원의 둘레와 넓이 구하기
circle = Circle(10)

print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

# __radius에 접근
# print("# __radius에 접근합니다")
# print(circle.__radius)

""" 속성 선언시 __를 앞에 붙이면 외부에서 사용 불가능
Traceback (most recent call last):
  File "C:\python\코딩연습\basic\추가정보\private_var.py", line 22, in <module>
    print(circle.__radius)
AttributeError: 'Circle' object has no attribute '__radius'
"""

# 간접적으로 __radius에 접근
print(circle.get_radius())
print()

circle.set_radius(2)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()