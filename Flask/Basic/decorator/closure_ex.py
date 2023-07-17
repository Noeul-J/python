"""
closure function
- 함수와 해당 함수가 가지고 있는 데이터를 함께 복사, 저장해서 별도 함수로 활용하는 기법으로 First-class 함수와 동일
- 외부 함수가 소멸되더라도, 외부 함수에 안에 있는 로컬 변수 값과 중첩함수(내부함수)를 사용할 수 있는 기법
"""


def calc_power(n):
    def power(digit):
        return digit ** n
    return power


list_data = list()
for num in range(1, 6):
    list_data.append(calc_power(num))

for func in list_data:
    print(func(2))


