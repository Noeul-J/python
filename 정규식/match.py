import re
import sys

# 정규식 패턴과 문자열을 받아 match 결과를 반환
def reg(pattern, text):
    result = re.match(pattern, text)
    if result:
        print('Match found: ', result.group())
        return result.group()
    else:
        print('No match')
        return "No"

if __name__ == '__main__':
     # 웍디에서 정규식 패턴과 문자열을 받아옴
     pattern = sys.argv[1]
     text = sys.argv[2]

     # pattern = '[a-z]+'
     # text = "python"
     print("찾는 패턴: %s, 문자열: %s" % (pattern, text))
     regResult = reg(pattern, text)

     # 웍디로 결과값을 넘김
     print("<peon>")
     print(regResult)
     print("</peon>")
