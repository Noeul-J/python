import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # [ 산점도 ]
# plt.rcParams.update({'figure.dpi'     : '150',
#                      'figure.figsize' : [8, 6],
#                      'font.size'      : '15',
#                      'font.family'    : 'Malgun Gothic'})
# # 해상도, 기본값 72,
# # 그림 크기, 기본값 [6, 4],
# # 글자 크기, 기본값 10
# # 폰트, 기본값 sans-serif
#
# # 모든 설정 되돌리기
# plt.rcParams.update(plt.rcParamsDefault)
#
# mpg = pd.read_csv('mpg.csv')
# sns.scatterplot(data=mpg, x='displ', y='hwy')
#
# # 축 범위 설정하기
# sns.scatterplot(data=mpg, x='displ', y='hwy')\
#     .set(xlim = [3, 6], ylim=[10, 30])
#
# # 종류별로 표식 색깔 바꾸기
# sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
# plt.show()

# # [평균 막대 그래프]
# # 집단별 평균표 만들기
mpg = pd.read_csv('mpg.csv')
# df_mpg = mpg.groupby('drv', as_index=False)\
#             .agg(mean_hwy = ('hwy', 'mean'))
# df_mpg = df_mpg.sort_values('mean_hwy', ascending=False)
# sns.barplot(data=df_mpg, x='drv', y='mean_hwy')
# plt.show()

# # [빈도 막대 그래프]
# df_mpg = mpg.groupby('drv', as_index=False)\
#              .agg(n=('drv', 'count'))
# sns.countplot(data=mpg, x='drv')
# plt.show()

# # [시계열 그래프]
# economics = pd.read_csv('economics.csv')
# sns.lineplot(data=economics, x='date', y='unemploy')
#
# economics['date2'] = pd.to_datetime(economics['date'])
# economics['year'] = economics['date2'].dt.year
# print(economics.head())
# # economics['month'] = economics['date2'].dt.month
# # economics['day'] = economics['date2'].dt.dav
# sns.lineplot(data=economics, x='year', y='unemploy', ci=None) \
#     .set(xlim=[1970, 2010])
# plt.show()

# [상자 그림]
sns.boxplot(data=mpg, x='drv', y='hwy')
plt.show()