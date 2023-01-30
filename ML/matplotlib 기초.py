import matplotlib.pyplot as plt     # pip3 install matplotlib
import pandas as pd
import random
# print(plt.style.available)      # matplotlib에서 사용할 수 있는 스타일시트 목록 출력


series = pd.Series(random.sample(range(100, 1000), 10), index = list('matplotlib'))

plt.style.use("default")
plt.bar(series.index, series.values)
plt.show()