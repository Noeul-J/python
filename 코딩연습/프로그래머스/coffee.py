"""
2023.01.19

가진 돈으로 마실 수 있는 최대 잔 수와 남는 돈
divmod 함수 이용
"""
def solution(money):
    # answer = []
    # coffee = int(money/5500)
    # charge = money%5500
    # answer = [coffee, charge]
    # return answer

    return divmod(money, 5500)  #(25, 2500)

if __name__ == '__main__' :
    americano = solution(140000)
    print(americano)