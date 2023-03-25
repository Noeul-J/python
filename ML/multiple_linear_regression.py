"""
2023-03-25 다중 선형 회귀

다중 선형 회귀(Multiple Linear Regression, MLR)는 여러 개의 독립 변수와 하나의 종속 변수의 선형 관계를 모델링하는 것
y = W1x1+W2x2+...+Wnxn + b

다중 선형 회귀를 사용할 땐 다음과 같은 가정들이 필요하다.

1. 각각의 독립 변수는 종속 변수와의 선형 관계가 존재한다. (y=Wixi 그래프를 그렸을 때 직선의 형태)
2. 독립 변수 사이에서는 높은 수준의 상관관계가 존재하지 않아야 한다. 만약 그렇지 않다면 관계를 분석하기가 어렵다.
3. 추정된 종속 변수의 값과 실제 관찰된 종속 변수의 값과의 차이, 즉 잔차(residual)가 정규 분포를 이루어야 한다.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://bit.ly/perch_csv")
perch_full = df.to_numpy()
print(perch_full)

# [[ 8.4   2.11  1.41]
#  [13.7   3.53  2.  ]
#  [15.    3.82  2.43]
#  [16.2   4.59  2.63]
#  [17.4   4.59  2.94]
#  [18.    5.22  3.32]
#  [18.7   5.2   3.12]
#  ...] -- 길이, 높이, 너비

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state = 42)

# PolynomialFeatures 클래스는 입력 데이터 x를 [1, x, x^2, x^3, ...] 과 같이 여러 다항식으로 변환
# 만약 입력 데이터가 x,y이면 [1, x, y, x^2, y^2, xy, x^3, y^3, X^2y,...] 와 같이 변환
# 차수를 결정하는 degree와 상수항 생성 여부를 결정하는 include_bias를 매개변수로 갖는다
# poly = PolynomialFeatures(include_bias=False)
# poly.fit([[2, 3]])
# print(poly.transform([[2, 3]])) # [[2. 3. 4. 6. 9.]]

poly = PolynomialFeatures(degree=2, include_bias=False)        # 차수를 올리면 훈련 셋은 거의 완벽해지지만, 테스트 셋의 점수가 음수로 나올수도 있음(과대 적합)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)
print(train_poly.shape)            # (42, 9) -- 3개의 샘플(길이, 높이, 너비)이 9개로 변환됨
# 기존의 특성을 사용해 새로운 특성을 뽑아내는 작업 - 특성 공학(Feature engineering)
print(poly.get_feature_names_out()) # ['x0' 'x1' 'x2' 'x0^2' 'x0 x1' 'x0 x2' 'x1^2' 'x1 x2' 'x2^2']

lr = LinearRegression()
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))



