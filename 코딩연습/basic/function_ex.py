import random

# # n! = n * (n-1) * (n-2) * ... * 1
# def factorial(n):
#     output = 1
#
#     for i in range(1, n+1):
#         output *= i
#
#     return output
#
#
# print(factorial(5))


# # 재귀함수를 통한 팩토리얼
# def factorial_recursion(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_recursion(n-1)
#
#
# print(factorial_recursion(5))


# # 피보나치 수열
# counter = 0
#
# def fibonacci(n):
#     global counter
#     counter += 1
#
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(10))

# # 메모화
# dictionary = {
#     1: 1,
#     2: 1
# }
#
# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     output = fibonacci(n-1) + fibonacci(n-2)
#     dictionary[n] = output
#     return output
#
# print(fibonacci(10))

# # 함수의 매개 변수로 함수 전달하기
# def call_10_times(func):
#     for i in range(10):
#         func()
#
#
# def print_hello():
#     print("안녕")
#
#
# call_10_times(print_hello)
#
# map(), filter()
# def power(item):
#     return item * item
#
#
# def under_3(item):
#     return item < 3
#
#
# # power = lambda x : x * x
# # under_3 = lambda x : x < 3
#
#
# list_input_a = [1, 2, 3, 4, 5]
#
# # map 함수 사용
# output_a = map(power, list_input_a)
# print("# map()의 실행 결과")
# print("map(power, list_input_a): ", output_a)
# print("map(power, list_input_a): ", list(output_a))
# print()
#
# # filter 함수 사용
# output_b = filter(under_3, list_input_a)
# print("# filter()의 실행 결과")
# print("filter(under_3, list_input_a): ", output_b)
# print("filter(under_3, list_input_a): ", list(output_b))

# # 파일 처리
# # w - write, a - append, r - read
# file = open("C:\\python\\test2.txt", "w")
# file.write("Hello Python Programming..!")
# file.close()
#
# with open("C:\\python\\test2.txt", "w") as file:       # 파일을 자동으로 열고 닫아줘
#     file.write("Hello Python Programming..!")
#
# with open("C:\\python\\test2.txt", "r") as file:
#     contents = file.read()
#
# print(contents)

# # 랜덤하게 1000명의 키와 몸무게 만들기
# hanguls = list("가나다라마바사아자차카타파하")
#
# with open("C:\\python\\info.txt", "w") as file:
#     for i in range(1000):
#         # 랜덤한 값으로 변수 생성
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)
#
#         # 텍스트 쓰기
#         file.write("{}, {}, {}\n".format(name, weight, height))
#
# with open("C:\\python\\info.txt", "r") as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(",")
#
#         # 데이터가 문제 있는지 확인
#         if (not name) or (not weight) or (not height):
#             continue
#
#         bmi = int(weight) / ((int(height) / 100) ** 2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
#
#         # 출력
#         print('\n'.join([
#             "이름: {}",
#             "몸무게: {}",
#             "키: {}",
#             "BMI: {}",
#             "결과: {}"
#         ]).format(name, weight, height, bmi, result))
#         print()

# # 제너레이터 함수
def test():
    print("함수가 호출되었다")
    yield "test"


print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())



