# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):                                        # eq 같다, ne 다르다, gt 크다, ge 크거나 같다, lt 작다, le 작거나 같다
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


students = [
    {"name" : "홍길동", "korean": 87, "math" : 99, "english": 100, "science": 87},
    {"name" : "연하진", "korean": 87, "math" : 99, "english": 100, "science": 87},
    {"name" : "구지연", "korean": 87, "math" : 99, "english": 100, "science": 87},
    {"name" : "나선주", "korean": 87, "math" : 99, "english": 100, "science": 87},
    {"name" : "윤아린", "korean": 87, "math" : 99, "english": 100, "science": 87},
    {"name" : "윤인성", "korean": 87, "math" : 99, "english": 100, "science": 87},
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    print(student)
    info = Student(student["name"], student["korean"], student["math"], student["english"], student["science"])
    print(str(info))