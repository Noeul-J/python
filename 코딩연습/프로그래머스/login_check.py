"""
2023.01.19

db에 저장된 데이터를 이용해
id 값이 있는데 pw가 다르면 "wrong pw"
id 값도 없으면 "fail"
맞는 정보면 "login" 출력
"""
def solution(id_pw, db):
    ac_dic = {}
    answer = ''

    for id, pw in db:
        ac_dic[id] = pw

    if ac_dic.get(id_pw[0]):
        if id_pw[1] == ac_dic[id_pw[0]]:
            answer = "login"
        else:
            answer = "wrong pw"
    else:
        answer = "fail"

    return answer

if __name__ == '__main__' :
    id_pw = ["meosseugi", "1234"]
    db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
    result = solution(id_pw, db)
    print(result)