a = set([1,2,3,4,5,6])
b = set([5,6,7,8,9,10])

print(a & b)    # 교집합
print(a | b)    # 합집합
print(a - b)    # 차집합

print(a.intersection(b))    # 교집합
print(a.union(b))              # 합집합
print(a.difference(b))      # 차집합

# 집합에 값 추가
a.add(22)
a.update([11, 33, 44])
print(a)

# 집합 값 삭제
a.remove(33)    # 삭제할 값을 입력. 값이 없으면 에러 발생
a.discard(33)   # 값이 없어도 에러 발생하지 않음
print(a)

a.pop()         # 가장 앞의 값을 삭제
print(a)