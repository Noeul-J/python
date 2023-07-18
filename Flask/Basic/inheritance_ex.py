# # 상속

# class Figure:
#     def __init__(self, name, color):        # 생성자
#         self.name = name
#         self.color = color
    
# class Quadrangle(Figure):
#     def set_area(self, width, height):
#         self.width = width
#         self.height = height
        
        
#     def get_info(self):
#         print(self.name, self.color, self.width * self.height)
        

# square = Quadrangle('Tom', 'green')
# square.set_area(5, 5)
# print(square.get_info())

# # https://pythontutor.com/visualize.html#mode=edit -- 구조 확인 가능
# # Quadrangle 클래스가 Figure 클래스의 자식 클래스인지 확인
# print(issubclass(Quadrangle, Figure))

# # 해당 클래스가 해당 객체에서 나온건지 확인
# figure1 = Figure('figure1', 'black')
# square = Quadrangle('square', 'red')
# print(isinstance(figure1, Quadrangle))
# print(isinstance(square, Quadrangle))

# # 메서드 재정의 - 자식 클래스에서 부모 클래스
# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def work(self):
#         print (self.name + " works hard")
        
# class Student(Person):
#     def work(self):
#         print(self.name + " studies hard")
        
#     def go_to_school(self):
#         print('Go to school')
        

# student1 = Student("Alice")
# print(student1.work())          # 자식 클래스의 재정의된 work(self) 호출

# p1 = Person("alice")
# s1 = Student("alice")

# p1.work()
# s1.work()
# s1.go_to_school()


# # 실습
# class Car:
#     def __init__(self, name):
#         self.name = name
        
#     def get_info(self):
#         print(self.name)
        
# class EletronicCar(Car):
#     def get_info(self):
#         print(self.name, 'Fuel:Eletronic')
        
# class GasolineCar(Car):   
#     def get_info(self):
#         print(self.name, 'Fuel:gasoline')


# car = Car('HyunDae')
# car.get_info()
# el_car = EletronicCar('Honda')
# el_car.get_info()
# gas_car = GasolineCar('Gia')
# gas_car.get_info()

# # super
# class Person:
#     def work(self):
#         print ("works hard")
    
# class Student(Person):
#     def work(self):
#         print("studies hard")
    
#     def go_to_school(self):
#         super().work()
    
# student1 = Student()
# student1.work()
# student1.go_to_school()


# # 클래스의 속성
# class Figure:
#     count = 0       # 클래스 변수
    
#     # 생성자(initializer)
#     def __init__(self, width, height):
#         # self.* : 인스턴스 변수
#         self.width = width
#         self.height = height
#         # 클래스 변수 접근 예
#         Figure.count += 1
        
#     def __del__(self):
#         Figure.count -= 1
        
#     # 메서드
#     def calc_area(self):
#         return self.width * self.height
    
# figure = Figure(2, 3)
# print(figure.count)
# figure2 = Figure(2, 3)
# print(Figure.count)


# # static method
# class Figure:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
        
#     def calc_area(self):
#         return self.width * self.height
    
#     # 정적 메서드(Figure에 너비와 높이가 같은 도형은 정사각형임을 알려주는 기능)
#     @staticmethod
#     def is_square(rect_width, rect_height):
#         if rect_width == rect_height:
#             print("정사각형이 될 수 있는 너비/높이입니다.")
#         else:
#             print("정사각형이 될 수 없는 너비/높이입니다.")
            
# figure1 = Figure(2, 3)
# figure1.is_square(5, 5)         # 객체명.정적 메서드명으로 호출 가능
# Figure.is_square(4, 5)          # 클래스명.정적메서드명으로 호출 가능


# class Figure:
#     count = 0       # 클래스 변수

#     # 생성자(initializer)
#     def __init__(self, width, height):
#         # self.* : 인스턴스 변수
#         self.width = width
#         self.height = height
#         # 클래스 변수 접근 예
#         Figure.count += 1

#     @staticmethod
#     def print_count():
#         print(Figure.count)

#     @staticmethod       # 에러: 정적 메서드에서는 객체 attribute는 접근 불가
#     def print_width():
#         print(self.width)

# figure1 = Figure(1, 2)
# print(Figure.count)
# print(figure1.print_count())
# # print(figure1.print_width())


# # class method
# class Figure1:
#     count = 0       # 클래스 변수

#     # 생성자(initializer)
#     def __init__(self, width, height):
#         # self.* : 인스턴스 변수
#         self.width = width
#         self.height = height
#         # 클래스 변수 접근 예
#         Figure1.count += 1
        
#     def calc_area(self):
#         return self.width * self.height
    
#     # 클래스 메서드
#     @classmethod
#     def print_count(cls):
#         # print(self.width)   # 에러: 정적 메서드에서는 객체 attribute는 접근 불가
#         return cls.count
    

# figure1 = Figure1(2, 3)
# figure2 = Figure1(4, 5)
# print(Figure1.count)
# print(Figure1.print_count())
# print(figure1.print_count())

# static method와 class method 범위
# -- class method는 class 내, static은 전체
class Figure:
    @classmethod
    def set_name(cls, name):
        cls.name = name
        
class Circle(Figure):
    pass

Figure.set_name('figure')
print(Figure.name, Circle.name)

Circle.set_name('circle')
print(Figure.name, Circle.name)

# figure figure
# figure circle

class Triangle:
    @staticmethod
    def set_name(name):
        Triangle.name = name

class Circle(Triangle):
    pass

Triangle.set_name('triangle')
print(Triangle.name, Circle.name)
Circle.set_name('circle')
print(Triangle.name, Circle.name)

# triangle triangle
# circle circle