class Student:
    count = 0
    students =[]

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------- 학생 목록 -------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------ -------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


# 학생 리스트를 선언
Student("윤인성", 87, 99, 20, 45)
Student("연하진", 87, 99, 20, 45)
Student("구지연", 87, 99, 20, 45)
Student("나선주", 87, 99, 20, 45)
Student("윤아린", 87, 99, 20, 45)
Student("윤명월", 87, 99, 20, 45)


# 현재 생성된 학생들을 모두 출력
Student.print()