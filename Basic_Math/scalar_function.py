import numpy as np
import matplotlib.pyplot as plt

# Figure를 추가
fig = plt.figure(figsize=(7,7))

#3DAxes를 추가
ax = fig.add_subplot(projection='3d')

ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='z', labelsize=15)

# 측 라벨을 설정
ax.set_xlabel('$x_1$', fontsize=20)
ax.set_ylabel('$x_2$', fontsize=20)
ax.set_zlabel('$z$', fontsize=20)

x1 = np.linspace(-2, 2, 50)             
x2 = np.linspace(-1, 3, 50)             
X1, X2 = np.meshgrid(x1, x2)                   #x1, x2의 교차점을 찾아 (x1, x2) 조합으로 평면에 있는 한 점을 만듦
Z = 50*(X2 - X1**2)**2 + (2 - X1)**2


# ax.scatter3D(X1, X2, Z, marker='.', color='gray')
ax.plot_surface(X1, X2, Z, cmap=plt.cm.binary, edgecolor="k")       # 평면으로 그래프를 그림
plt.show()