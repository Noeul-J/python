import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# pip install pyreadstat
raw_welfare = pd.read_spss('Koweps_hpwc14_2019_beta2.sav')
welfare = raw_welfare.copy()

# print(welfare.shape)      # 행, 열 개수
# print(welfare.describe())  # 요약 통계량

# 변수명 변경
welfare = welfare.rename(columns = {'h14_g3'     : 'sex',            #  성별
                                    'h14_g4'     : 'birth',          #  태어난 연도
                                    'h14_g10'    : 'marriage_type',  #  혼인 상태
                                    'h14_g11'    : 'religion',       #  종교
                                    'p1402_8aq1' : 'income',         #  월급
                                    'h14_eco9'   : 'code_job',       #  직업 코드
                                    'h14_reg7'   : 'code_region'})   #  지역 코드

# sns.histplot(data=welfare, x='income')      #히스토그램 만들기
# plt.show()

sex_income = welfare.dropna(subset=['income'])\
                    .groupby('sex', as_index=False)\
                    .agg(mean_income = ('income', 'mean'))
sns.barplot(data=sex_income, x='sex', y='mean_income')
plt.show()