class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다".format(Student.count))

# 학생 리스트 선언
students = [
    Student("윤인성", 87, 99, 20, 45),
    Student("연하진", 87, 99, 20, 45),
    Student("구지연", 87, 99, 20, 45),
    Student("나선주", 87, 99, 20, 45),
    Student("윤아린", 87, 99, 20, 45),
    Student("윤명월", 87, 99, 20, 45)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다".format(Student.count))