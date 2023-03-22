class Student:
    def study(self):
        print("공부하자")


class Teacher:
    def teach(self):
        print("학생 가르친다")


classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()