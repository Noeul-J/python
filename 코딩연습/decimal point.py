# format(값, "형식규칙") or "{형식규칙}".format(값)

# # 1000 마디 마다 , 찍기
# a = 12345678910
# b = format(a, ',')
# print(b)

# # 1000 마디 마다 , 찍기(정수형)
# a = 12345678910
# b = format(a, ',d')
# print(b)

# # 1000 마디 마다 , 찍기(실수형) -- 소수점 아래 5자리까지 표시
# a = 12345678910
# b = 1000000.408
#
# af = format(a, ',f')
# bf = format(b, ',f')
# print(af)
# print(bf)

# # "{형식규칙}".format(값) 쓰기
# a = 12345678910
# b = 100000.406234
# af = '{0:,}'.format(a)
# bf = '{0:,}'
# c = "{:0,.1f}".format(a)    # 소수점 한자리 까지 출력 - 둘째자리에서 반올림
# d = "{:0,.3f}".format(b)    # 소수점 셋째자리 까지 출력 - 넷째자리에서 반올림
# print(af)
# print(bf)
# print(c)
# print(d)





