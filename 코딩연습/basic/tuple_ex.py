# 튜플 -- 수정이 안됨

# 요소를 하나만 가지는 튜플
tup = (273,)        # (273) X

# 리스트와 튜플 선언
[a, b] = [1, 2]
(c, d) = (10, 20)

print(c)

# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("tuple_test: ", tuple_test)
print(type(tuple_test))

a, b, c = 10, 20, 30
print("b: ", b)

# 변수 값 교환
a, b = b, a
print("a: {}, b: {}".format(a, b))


def ddd():
    return 10, 20


h, i = ddd()
print("h: {}, i: {}".format(h, i))


