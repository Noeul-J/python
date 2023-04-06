"""
2023-03-27

로지스틱 회귀(Logistic Regression)
- 회귀를 사용하여 데이터가 어떤 범주에 속할 확률을 0에서 1사이의 값으로 예측하고
그 확률에 따라 가능성이 더 높은 범주에 속하는 것으로 뷴류해주는 지도 학습 알고리즘

2진분류(binary classification)

- 모든 속성(feature)들의 계수(coefficient)와 절편(intercept)을 0으로 초기화한다
- 각 속성들의 값(value)에 계수(coefficient)를 곱해서 log-odds를 구한다.
- log-odds를 sigmoid 함수에 넣어서 [0,1] 범위의 확률을 구한다.

odds = 사건이 발생할 확률 / 사건이 발생하지 않을 확률

"""