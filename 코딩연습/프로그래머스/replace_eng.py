"""
2023.01.19

영어로 된 글자를 숫자로 치환
맨 앞에 0이 올 수는 없음
"""
def solution(numbers):
    numbers = numbers.replace('one', '1')
    numbers = numbers.replace('two', '2')
    numbers = numbers.replace('three', '3')
    numbers = numbers.replace('four', '4')
    numbers = numbers.replace('five', '5')
    numbers = numbers.replace('six', '6')
    numbers = numbers.replace('seven', '7')
    numbers = numbers.replace('eight', '8')
    numbers = numbers.replace('nine', '9')
    numbers = numbers.replace('zero', '0')

    if numbers.startswith('0'):
        numbers = numbers.replace('0', '', 1)
        numbers.strip()

    answer = int(numbers)
    return answer

if __name__ == '__main__':
    result = solution("onetwothreefourfivesixseveneightnine")
    print(result)