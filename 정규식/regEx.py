import re
import sys

# 정규식 패턴 가져옴
def set_pattern(patternCode):
    if patternCode == '소문자':
        pattern = '[a-z\s]+'
    elif patternCode == '대문자':
        pattern = '[A-Z\s]+'
    elif patternCode =='영어':
        pattern = '[a-z | A-Z\s]+'
    elif patternCode == '한글':
        pattern = '[가-횧\s]+'
    elif patternCode == '숫자':
        pattern = '[0-9\s]+'
    elif patternCode == '특수문자제거':
        pattern = '[\w\s]'
    else:
        pattern = patternCode

    return pattern

# 패턴과 문자열을 이용해 원하는 부분 추출
def reg(pattern, text):
    result = re.findall(pattern, text)

    count = 0
    for r in result:
        if r == ' ':
            count = count + 1

    print('띄어쓰기 빈칸 개수: ', count)

    # 정규식과 일치하는 데이터가 있으면 문자열을, 데이터가 없으면 "No" 반환
    if len(result) == count:
        # 결과에 띄어쓰기 빈칸만 존재할 때
        print('No match')
        return "No"

    elif len(result) > 0:
        # 리스트 결과값 하나의 문자열로 변환
        print('Match found: ', str(result))
        resultText = ''

        for t in result:
            if t == result[0]:
                resultText = t
            else:
                resultText = resultText + t
        return resultText
    else: # 결과 없을 때
        print('No match')
        return "No"

if __name__ == '__main__':
    # patternCode = '영어'
    # text = "Python !@한글#abc?"

    # 웍디에서 값을 받아옴
    patternCode = sys.argv[1]
    text = sys.argv[2]
    print("찾는 패턴 코드: %s" % (patternCode))


    p = set_pattern(patternCode)
    print("찾는 패턴: %s, 문자열: %s" % (p, text))
    regResult = reg(p, text)

    print("<peon>")
    print(regResult)
    print("</peon>")
