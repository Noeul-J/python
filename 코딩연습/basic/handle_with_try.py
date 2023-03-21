# try:
#     r = int(input("정수 입력: "))
#
#     print("반지름: ", r)
#     print("원의 둘레: ", 2 * 3.14 * r)
#     print("원의 넓이: ", 3.14 * r * r)
#
# except:
#     print("무언가 오류 발생")
#     pass  #그냥 넘겨
# else:
#         # 예외가 발생하지 않았을 때 실행할 코드
#             # 예외 생기는 코드만 try에 넣어놓아
# finally:
#     # 무조건 실행하는 코드

# # try 구문 내부에 return 키워드가 있는 경우 finally를 쓰면 좀 더 깔끔해짐
# def write_text_file(filename, text):
#     try:
#         file = open(filename, "w")
#         file.write(text)
#         return
#     except Exception as e:
#         print(e)
#     finally:
#         file.close()
#
# write_text_file("test.txt", "안녕하세요")

# list_number = [52, 273, 72, 33, 44, 623]
#
# try:
#     number_input = int(input("정수 입력: "))
# except ValueError as exception:
#     print("정수를 입력해라")
#     print(type(exception), exception)
# except IndexError as exception:
#     print("리스트의 인덱스를 벗어남")
#     print(type(exception, exception))
# except Exception as exception:
#     print("미리 파악하지 못한 예외가 발생함")
#     print(type(exception), exception)