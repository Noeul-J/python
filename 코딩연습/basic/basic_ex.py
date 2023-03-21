import datetime
import time

"""
[문자열]
"""
#
# # 문자열 연결 시 +로
# print("내 목표는 " + "퇴사")
#
# # 문자열 반복은 *
# print("퇴사" * 3)
#
# # 문자열 인덱스 0부터 시작
# print("이직을 합시다"[5])
#
# # 거꾸로 할 때는 -1부터
# print("이직을 합시다"[-2])
#
# # 문자열 슬라이싱 - 첫번째 ~ 마지막-1
# print("이직을 합시다"[1:4])
# print("이직을 합시다"[1:])
# print("이직을 합시다"[:4])
#
# # 문자열 길이 구하기
# print(len("이직을 합시다"))

"""
[숫자]
"""

# # 지수 표현
# print(0.52273e2)
# print(0.52273e-2)
#
# # 정수 나누기 연산자 // -- 몫을 정수로(소수점 아래 버림)
# print("3//2 = ", 3//2)
#
# # 나머지 %
# print("15%2 = ", 15%2)
#
# # 제곱 **
# print("2**2 = ", 2**2)


"""
[변수]
"""

# # 복합 대입 연산자
# number = 100
# number += 10
# number += 20
# number += 30
# print("number : ", number)
#
# string = "안녕하세요"
# string += "!"
# string += "!"
# print("string: ", string)
#
# # 사용자 입력 받기 -- 입력받은 것들은 모두 문자열로 인식됨
# string = input("인사말을 입력하세요: ")
# print(string)
#
# # 형변환
# string_a = input("A 입력 : ")
# int_a = int(string_a)
#
# string_b = input("B 입력 : ")
# int_b = int(string_b)
#
# print("문자열 자료 : ", string_a + string_b)
# print("숫자 자료 : ", int_a + int_b)
#
# input_a = float(input("첫번째 숫자: "))
# input_b = float(input("두번째 숫자: "))
#
# print("곱셈 결과 : ", input_a * input_b)
#
# fl = float("47.123")
# num = int(fl)
# print(num)
#
# val = int("47.123") --  소수점 있는 걸 바로 int 하면 오류 남
#
# strNum = str(52.273)
# print(strNum)

"""
[자료형]
"""

# # format() 함수
# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 연봉 {}만 원 만들기".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)
#
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)
#
# # 정수를 특정 칸에 출력
# output_a = "{:d}".format(52)
#
# # 특정 칸에 출력하기
# output_b = "{:5d}".format(52)       # 5칸
# output_c = "{:10d}".format(52)      # 10칸
# output_d = "{:05d}".format(52)      # 양수
# output_e = "{:05d}".format(-52)     # 음수
#
# print("# 기본")
# print(output_a)
# print("# 특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("# 빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)
#
# # 기호 붙여 출력하기
# output_f = "{:+d}".format(52)
# output_g = "{:+d}".format(-52)
# output_h = "{: d}".format(52)
# output_i = "{: d}".format(-52)
#
# print("# 기호 붙여 출력하기")
# print(output_f)
# print(output_g)
# print(output_h)
# print(output_i)
#
# # format 조합
# output_h = "{:+5d}".format(52)          # 기호를 뒤로 밀기    +52
# output_i = "{:+5d}".format(-52)
# output_j = "{:=+5d}".format(52)         # 기호를 앞으로 밀기  +  52
# output_k = "{:=+5d}".format(-52)
# output_l = "{:+05d}".format(52)         # 0으로 채우기       +0052
# output_m = "{:+05d}".format(-52)
#
# print("# 조합하기")
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print(output_l)
# print(output_m)
#
# # float 자료형 기본
# output_a = "{:f}".format(52.273)
# output_b = "{:15f}".format(52.273)      # 15칸 만들기                             52.273000
# output_c = "{:+15f}".format(52.273)     # 15칸에 부호 추가하기                     +52.273000
# output_d = "{:+015f}".format(52.273)    # 15칸에 부호 추가하고 0으로 채우기     +0000052.273000
#
# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)
#
# # 소수점 아래 자릿수 지정하기
# output_a = "{:15.3f}".format(52.273)                        #         52.273
# output_b = "{:15.2f}".format(52.273)                        #          52.27
# output_c = "{:15.1f}".format(52.273)                        #           52.3
#
# print(output_a)
# print(output_b)
# print(output_c)
#
# # 의미 없는 소수점 제거하기
# output_a = 52.0
# output_b = "{:g}".format(output_a)
# print(output_a)
# print(output_b)
#
# # 대소문자 바꾸기
# a = "Hello Python Programming!"
# print(a.upper())
# print(a.lower())
#
# # 문자열 양 옆 공백 제거하기
# input_a = """
#     안녕하세요
# 문자열의 함수를 알아봅시다
# """
# print(input_a.strip())
#
# # 문자열의 구성 파악하기
# """
# isalnum():문자열이 알파벳 또는 숫자로만 구성되어 있는지
# isalpha():문자열이 알파벳으로만 구성되어 있는지
# isidentifier():문자열이 식별자로 사용할 수 있는 것인지
# isdecimal(): 문자열이 정수 형태인지
# isdigit(): 문자열이 숫자로 인식될 수 있는지
# isspace(): 문자열이 공백으로만 구성되어 있는지
# islower(): 문자열이 소문자로만 구성되어 있는지
# isupper(): 문자열이 대문자로만 구성되어 있는지
# """
# print("TrainA10".isalnum())
# print("10".isdigit())
#
# 문자열 찾기
# output_a = "안녕안녕하세요".find("안녕")         # 왼쪽부터 찾아서 처음 등장하는 위치
# print(output_a)                               # 0
# output_b = "안녕안녕하세요".rfind("안녕")        # 오른쪽부터 찾아서 처음 등장하는 위치
# print(output_b)                               # 2
#
# print("안녕" in "안녕하세요")
# print("잘자" in "안녕하세요")
#
# # 문자열 자르기
# a = "10 20 30 40 50 60".split(" ")
# print(a)

"""
[시간]
"""
# now = datetime.datetime.now()
#
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
#
# # 오전과 오후 나누기
# if now.hour < 12 :
#     print("현재시간은 {}시로 오전입니다".format(now.hour))
# else :
#     print("현재시간은 {}시로 오후입니다".format(now.hour))
#
# # 계절나누기
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다".format(now.month))
# elif 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다".format(now.month))
# elif 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다".format(now.month))
# else:
#     print("이번 달은 {}월로 겨을입니다".format(now.month))

"""
[불 자료형]
"""
# number = str(52)
# last_char = number[-1]
#
# if last_char in "02468":
#     print("작수입니다")
# else:
#     print("홀수입니다")
#
# # False로 변환되는 값  -- 0과 빈 문자열은 False로 반환
# print("# if 조건문에 0 넣기")
# if 0:
#     print("0은 True로 변환됩니다")
# else:
#     print("0은 False로 변환됩니다")
#
# print("#if 조건문에 빈 문자열 넣기")
# if "":
#     print("빈 문자열은 True로 변환됩니다")
# else:
#     print("빈 문자열은 False로 변환됩니다.")

"""
[미구현 시]  -- pass
"""
# number = 100
#
# if number > 1:
#     pass         # 미구현 상태일 때
#     raise NotImplementedError   # 미구현 상태일 때 강제 오류 발생
# else:
#     pass

"""
[리스트]
"""

# # 리스트 연결
# list_a = [273, 32, 103, "문자열", True, False]
# print(list_a[-2])           # True
# print(list_a[3][0])         # "문"
#
# list_a = [1,2,3]
# list_b = [4,5,6]
#
# print("list_a + list_b = ", list_a + list_b)
# print("list_a * 3 = ", list_a * 3)
# print()
#
# print("# 길이 구하기")
# print("len(list_a) = ", len(list_a))
#
# # 리스트 요소 추가하기
# list_a.append(4)
# print(list_a)
#
# list_a.insert(0, 10)        # 0번째에 10을 삽입
# print(list_a)
#
# list_a.extend([6,7,8])     # 한번에 여러 요소로를 추가할 때
# print(list_a)
#
# + 는 비파괴적 처리 -- 원래 변수에 영향을 안줘, extend()는 영향을 줘(파괴적 처리)
#
# # 리스트 요소 삭제
# list_a = [0,1,2,3,4,5]
# del list_a[1]
# print("del list_a[1]:", list_a)
#
# del list_a[3:6]
# print(list_a)
#
# list_a.pop(2)   #매개변수를 입력하지 않으면 마지막 요소 제거
# print("pop(2):", list_a)
#
# list_c = [1, 2, 1, 2]
# list_c.remove(2)            # 리스트에서 첫번째 2를 삭제
# print(list_c)               # [1, 1, 2]
#
# list_d = [0, 1, 2, 3, 4, 5]
# list_d.clear()
# print(list_d)               # []
#
# # 리스트 내부에 있는지 확인 in/not in
# list_a = [273, 32, 103, 57, 63]
# print(273 in list_a)
# print(66 not in list_a)

""" 
[반복문]
"""
# for i in range(5):
#     print("출력")
#
# array = [273, 32, 103, 59, 66]
#
# for element in array:
#     print(element)
#
# for character in "안녕하세요":
#     print("-", character)

"""
[딕셔너리와 반복문]
"""
# # 딕셔너리 선언
# dictA = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin" : "필리핀"
# }
#
# print("이름은 {}, type은 {}, 재료는 {}, 원산지 {}".format(dictA["name"], dictA['type'], dictA['ingredient'], dictA['origin']))
#
# dictA["name"] = "8D 건조 망고"
# print(dictA["name"])
#
# # 딕셔너리에 값 추가/제거
# dictB = {}
# print("요소 추가 이전:", dictB)
#
# dictB["name"] = "새로운 이름"
# dictB["head"] = "새로운 정신"
# dictB["body"] = "새로운 몸"
#
# print("요소 추가 이후:", dictB)
#
# del dictB["name"]
# del dictB["body"]
#
# print("요소 제거 이후:", dictB)
# # 딕셔너리 내부에 키가 있는지 확인
# dictC = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient" : ["망고", "설탕", "화학품"],
#     "origin" : "필리핀"
# }
#
# key = "aaa"
#
# if key in dictC:
#     print(dictC[key])
# else :
#     print("존재하지 않는 키에 접근하고 있습니다")
#
# # get() 함수
# value = dictC.get("존재하지 않는 키")
# value = dictC.get("name")           # 해당 키 값의 value를 가지고 옴
# print("값:", value)
#
# if value == None:
#     print("존재하지 않는 키에 접근하고 있습니다")
#
# for key in dictC:
#     print(key, ":", dictC[key])
# # 반복문
# for i in range(5):              # 0 ~ 4
#     print(str(i) + "= 반복변수")
# print()
#
# for i in range(5, 10):          # 5 ~ 9
#     print(str(i) + "= 반복변수")
# print()
#
# for i in range(0, 10, 3):       # 0, 3, 6, 9
#     print(str(i) + "= 반복변수")
# print()
#
# array = [273, 32, 63, 77, 89]
#
# for i in range(len(array)):
#     print("{}번째 반복: {}".format(i, array[i]))
#
# # 반대로 반복
# for i in range(4, 0 -1, -1):
#     print("현재 반복 변수: {}".format(i))
#
# for i in reversed(range(5)):
#     print("현재 반복 변수: {}".format(i))
# # while문
# while True:
#     print(".", end="")
#
# # 해당하는 값 모두 제거하기
# list_test = [1, 2, 1, 2]
# value = 2
#
# while value in list_test:
#     list_test.remove(value)
#
# print(list_test)
#
# # 5초동안 반복하기
# number = 0
#
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1
#
# print("5초동안 {}번 반복했습니다.".format(number))
#
# # continue 키워드
# numbers = [5, 15, 6, 7, 20]
#
# for number in numbers:
#     if number < 10:
#         continue
#     print(number)

"""
[문자열, 리스트, 딕셔너리와 관련된 기본 함수]
"""
# # 최솟값, 최대값, 모두 더한 값
# numbers = [103, 57, 273, 32, 77]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#
# # reversed() 함수로 리스트 뒤집기
# list_a = [1, 2, 3, 4, 5]
# list_reversed = reversed(list_a)
#
# for i in list_reversed:
#     print("-", i)
#
# # 이렇게 실행하면 두번째 반복문이 실행이 되지 않음 -- 제너레이터
# temp = reversed([1, 2, 3, 4, 5, 6])
#
# for i in temp:
#     print("첫번째 반복문: {}".format(i))
#
# for i in temp:
#     print("두번째 반복문: {}".format(i))
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# for i in reversed(numbers):
#     print("첫번째 반복문: {}".format(i))
#
# for i in reversed(numbers):
#     print("두번째 반복문: {}".format(i))
#
# # 확장 슬라이싱
# print(numbers[::-1])
#
# # enumerate()
# example_list = ['요소A', '요소B', '요소C']
# print(example_list)
# print()
#
# print(list(enumerate(example_list)))
# print()
#
# for i, value in enumerate(example_list):    # enumerate() 함수 사용시 반복변수를 i, value 형태로 사용 가능
#     print("{}번째 요소는 {}입니다".format(i, value))
#
# # 딕셔너리의 items() 함수
# example_dict = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C"
# }
#
# print("items():", example_dict.items())
# print()
#
# for key, element in example_dict.items():
#     print("dictionary[{}] = {}".format(key, element))
#
# # 리스트 내포
# """
# array = []
#
# for i in range(0, 20, 2):
#     array.append(i * i)
#
# print(array)
# """
# array = [i * i for i in range(0, 20, 2)]
# print(array)
#
# array = ["사과", "귤", "초콜릿", "바나나"]
# output = [fruit for fruit in array if fruit != "초콜릿"]
# print(output)
#
# # 여러 줄 문자열
# test = (
#     "이렇게 입력해도"
#     "하나의 문자열로 연결되어 "
#     "생성됩니다"
# )
#
# print(test)
# print(type(test))
#
# number = 100
#
# if number % 2 == 0 :
#     print((
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 짝수입니다"
#     ).format(number, number))
# else :
#     print((
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 홀수입니다"
#     ).format(number, number))
#
# if number % 2 == 0 :
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는(은) 짝수입니다"
#     ]).format(number, number))
# else :
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는(은) 홀수입니다"
#     ]).format(number, number))
#
# """
# 반복할 수 있는 것 : 이터러블 iterable
# 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체
# 리스트, 문자열 튜플, 딕셔너리 등등
# """
# # 이터레이터
# # reversed() 함수, next() 함수
# numbers = [1, 2, 3, 4, 5, 6]
# r_num = reversed(numbers)
#
# print("reversed_numbers: ", r_num)
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
#

"""
[함수]
"""
# # 가변 매개변수
# # 가변 메개변수 뒤에은 일반 매개변수가 올수 엇ㅂ고, 가변 매개변수는 하나만 사용가능
# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
#
# print_n_times(3, "안녕하세요", "즐거운", "파이썬")
#
# # 기본 매개변수
# # 매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본값
# # 기본 매개변수 뒤에는 일반 매개변수는 올 수 없음
# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)
#
# print_n_times("안녕하세요")
#
# # 매개변수 이름을 지정 해서 입력하는 매개변수 - 키워드 매개변수(ex, n)
#
#
# def sum_all(start, end):
#     output = 0
#
#     for i in range(start, end+1):
#         output += i
#
#     return output
#
# result = sum_all(0, 100)
# print(result)
