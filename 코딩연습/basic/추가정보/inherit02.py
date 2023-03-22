# 부모에 정의되어 있는 함수를 자식에서 다시 정의하는 것을 오버라이드(재정의)
# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self)
#         print("##########내가 만든 오류가 생성되었어요!!#########")
#
#     def __str__(self):
#         return "오류가 발생했어요"
#
# raise CustomException

# 사용자 정의 예외를 생성
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("#### 오류정보 ####")
        print("메시지:", self.message)
        print("값:", self.value)

# 예외 발생
try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()

