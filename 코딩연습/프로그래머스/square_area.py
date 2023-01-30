"""
2023.01.27

dots =  [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
직사각형 네 꼭짓점의 좌표가 주어질때(배열 dots), 직사각형의 넓이를 구해라
"""

def solution(dots):
    x_length = dots[1][0] - dots[0][0]
    y_length = dots[2][1] - dots[0][1]
    return x_length * y_length


if __name__ == "__main__":
    square = [[1, 1], [2, 1], [2, 2], [1, 2]]
    area = solution(square)
    print(area)