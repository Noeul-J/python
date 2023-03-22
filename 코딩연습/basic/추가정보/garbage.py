# 가비지 컬렉터
# 변수에 저장하지 않으면 사용하고 바로 삭제함
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

# Test("A")
# Test("B")
# Test("C")

"""
A - 생성되었습니다
A - 파괴되었습니다
B - 생성되었습니다
B - 파괴되었습니다
C - 생성되었습니다
C - 파괴되었습니다
"""

a = Test("A")
b = Test("B")
c = Test("C")

"""
A - 생성되었습니다
B - 생성되었습니다
C - 생성되었습니다
A - 파괴되었습니다
B - 파괴되었습니다
C - 파괴되었습니다
"""