import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import drawing_line as dl


mpl.style.use('bmh')                        # 그래프의 테마 설정
mpl.style.use('seaborn-v0_8-whitegrid')

fig = plt.figure(figsize=(10, 7))           # 크기 (10.7)인 그림 생성
ax = fig.add_subplot(1, 1, 1)               # 그림에 좌표축 생성
ax.xaxis.set_tick_params(labelsize=18)      # 좌표축에 표시되는 좌표값 숫자 크기 지정
ax.yaxis.set_tick_params(labelsize=18)
plt.xlabel('$x$', fontsize=25)              # 측 이름 지정
plt.ylabel('$y$', fontsize=25)

"""
정의역을 np.linspace(start, stop, num) 함수로 생성
start에서 시작하여 stop으로 끝나는 구간에서 num개 숫자를 등간격으로 생성하여 돌려줌.
"""
x = np.linspace(-3, 2, 10)
y = 2*x+4
ax.plot(x, y, 'k')                          # 평면에 점을 연속적으로 찍어 그래프를 그림. k 옵션은 검은색

dl.arrowed_spines(fig, ax)

plt.show()