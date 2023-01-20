"""
2023.01.20

문자열 복호화
code의 배수 위치에 있는 글자만 읽기
"""

def solution(cipher, code):
    answer = ''
    idx = 1
    for text in cipher:
        if idx % code == 0:
            answer = answer + text
        idx += 1

    return answer

if __name__ == '__main__' :
    cipher = "dfjardstddetckdaccccdegk"
    code = 4
    result = solution(cipher, code)
    print(result)
