class Quadrangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    def get_area(self):
        return self.width * self.height
    
    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2
        
class SingleWord:
    pass

print(dir(SingleWord))


# 객체 설정
square1 = Quadrangle(10, 5, 'red')
square2 = Quadrangle(7, 7, 'blue')
square = Quadrangle(2, 3, 'blue')

# 속성
print(square1.width, square1.height, square1.color)
print(square2.width, square2.height, square2.color)
square.set_area(5, 5)
print(square.width)

area = square1.get_area()
area2 = square2.get_area()
print(area, area2)