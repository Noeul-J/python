
# 딕셔너리 리턴
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
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
    # score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    # score_average = score_sum / 4
    #
    # print(student["name"], score_sum, score_average, sep="\t")
    print(student_to_string(student))