# # 그래프 해상도 설정
import matplotlib.pyplot as plt
# plt.rcParams.update({'figure.dpi' : '100'})

import pandas as pd
import numpy as np


# # [결측치 정제하기] - null 값 측정
# df = pd.DataFrame({'sex'    : ['M', 'F', np.nan, 'M', 'F'],
#                    'score'  : [5, 4, 3, 4, np.nan]})
# print(pd.isna(df).sum())    # 결측치 빈도 확인
#
# # 결측치 제거
# # ** df.dropna()로 쓰면 모든 변수에 결측치 없는 데이터만 추출
# df_nomiss = df.dropna(subset=['score', 'sex'])
# print(df_nomiss)
#
# # ** 결측치 제거하지 않고 분석하기
# result = df.groupby('sex').agg(mean_score=('score', 'mean'),
#                                sum_score = ('score', 'sum'))
# print(result)

# # [결측치 대체하기]
# exam = pd.read_csv('exam.csv')
# exam.loc[[2, 7, 14], ['math']] = np.nan     # 2, 7, 14행의 math에 NaN 할당
# print(exam)
# exam['math'] = exam['math'].fillna(55)      # math가 NaN이면 55로 대체
# print(exam['math'].isna().sum())            # 결측치 빈도 확인

# # [이상치 정제하기]
# df = pd.DataFrame({'sex'    : [1, 2, 1, 3, 2, 1],
#                    'score'  : [5, 4, 3, 4, 2, 6]})
# print(df['sex'].value_counts(sort=False).sort_index())
#
# # 1    3
# # 2    2
# # 3    1
# # Name: sex, dtype: int64
#
# # sex가 3이면 NaN 부여
# df['sex'] = np.where(df['sex'] == 3, np.nan, df['sex'])
# # score가 5보다 크면 NaN 부여
# df['score'] = np.where(df['score'] > 5, np.nan, df['score'])
# # sex, score 결측지 제거 후 sex별 분리해서 score 평균 구하기
# df = df.dropna(subset = ['sex', 'score'])\
#     .groupby('sex')\
#     .agg(mean_score = ('score', 'mean'))
#
# print(df)

import seaborn as sns

mpg = pd.read_csv('mpg.csv')

sns.boxplot(data=mpg, y='hwy')
# plt.show()
pct25 = mpg['hwy'].quantile(.25)
pct75 = mpg['hwy'].quantile(.75)

iqr = pct75 - pct25         # IQR

pct25 - 1.5 * iqr           # 하한 4.5
pct75 + 1.5 * iqr           # 상한 40.5

# 극단치 결측 처리
mpg['hwy'] = np.where((mpg['hwy'] < 4.5) | (mpg['hwy'] > 40.5), np.nan, mpg['hwy'])
mpg_mean = mpg.dropna(subset=['hwy'])\
    .groupby('drv')\
    .agg(mean_hwy = ('hwy', 'mean'))

print(mpg_mean)


