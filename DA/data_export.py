import pandas as pd
import numpy as np

# # [DataFrame 이용]
# df = pd.DataFrame({'sex'     : ['F', 'M', 'F', 'M'],
#                    'country' : ['Korea', 'China', 'Japan', 'USA']})
# result = df.query('sex == "F" & country == "Korea"')
# print(result)
#
# country = "China"
# result = df.query('country == @country')
# print(result)
#
# # ** 참고
# pd.set_option('display.max_rows', None)     # 모든 행 출력하도록 설정
# pd.set_option('display.max_columns', None)  # 모든 열 출력하도록 설정
# pd.reset_option('display.max_rows')     # 행 출력 제한 되돌리기
# pd.reset_option('display.max_columns')  # 열 출력 제한 되돌리기


# #[데이터 읽기]
# exam = pd.read_csv('exam.csv')
# print(exam.head())

# # [원하는 데이터 추출]
#
# # exam에서 nclass가 1인 경우만 추출
# nclass1 = exam.query('nclass == 1')
# print(nclass1)
#
# # exam에서 nclass가 1이 아닌 경우만 추출
# not_nclass1 = exam.query('nclass != 1')
# print(not_nclass1)
#
# # 1반이면서 수학 점수가 50 점 이상인 경우
# result = exam.query('nclass == 1 & math >= 50')
# print(result)
#
# # 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
# result = exam.query('math >= 90 | english >= 90')
# print(result)
#
# # 1, 3, 5반에 해당하면 추출
# result = exam.query('nclass in [1, 3, 5]')
# print(result)
#
# # 1반의 수학 점수 평균 구하기
# nclass1 = exam.query('nclass == 1')
# math_mean = nclass1['math'].mean()
# print(math_mean)
#
# # 여러 변수 추출
# result = exam[['nclass', 'math', 'english']]
# print(result)
#
# # 변수가 한개 일때 DataFrame 형태 유지
# result = exam[['math']]
# print(result)
#
# # 변수 제거하기
# result = exam.drop(columns=['math','english'])
# print(result)
#
# # [pandas 함수 조합]
# # math가 50 이상인 행만 추출한 다음 id, math 앞부분 5행까지 추출
# result = exam.query('math >= 50')[['id', 'math']].head()
# print(result)

# # [정렬]
# sort = exam.sort_values('math', ascending = True)    # math 오름차순 정렬 (False는 내림차순)
# print(sort)
# sort = exam.sort_values(['nclass', 'math'], ascending = [True, False])    # nclass 오름차순, math 내림차순 정렬
# print(sort)

# # [파생변수 추가]
# addCol = exam.assign(total = exam['math'] + exam['english'] + exam['science'],       # total 추가
#                      mean = (exam['math'] + exam['english'] + exam['science']) / 3)  # mean 추가
# print(addCol)
# exam = exam.assign(total = lambda x: x['math'] + x['english'] + x['science'],
#                    mean  = lambda x: x['total'] / 3)
# print(exam)

# addCol_npwhere = exam.assign(test = np.where(exam['science'] >= 60, 'pass', 'fail'))
# print(addCol_npwhere)

# [집단별로 요약]
# ** 반별로 수학 평균 구하기
# exam = exam.groupby('nclass', as_index = False)\
#            .agg(mean_math = ('math', 'mean'))    # as_index = False 변수를 인덱스로 바꾸지 않게 설정
# print(exam)
#
# exam = exam.groupby('nclass', as_index = False) \
#            .agg(mean_math   = ('math', 'mean'),
#                 sum_math    = ('math', 'sum'),
#                 median_math = ('math', 'median'),
#                 n           = ('nclass', 'count'))
# print(exam)
#
# # 모든 변수의 요약 통계량 한 번에 구하기
# result = exam.groupby('nclass').mean()
# print(result)

# # [데이터 합치기]
# ** 가로로 합치기
# test1 = pd.DataFrame({'id'      : [1, 2, 3, 4, 5],
#                       'midterm' : [60, 80, 70, 90, 85]})
#
# test2 = pd.DataFrame({'id'    : [1, 2, 3, 4, 5],
#                       'final' : [70, 83, 65, 95, 80]})
#
# # id 기준으로 합쳐서 total에 할당
# total = pd.merge(test1, test2, how='left', on='id')
# print(total)

# # ** 세로로 합치기
# group_a = pd.DataFrame({'id'   : [1, 2, 3, 4, 5],
#                         'test' : [60, 80, 70, 90, 85]})
#
# group_b = pd.DataFrame({'id'   : [6, 7, 8, 9, 10],
#                         'test' : [70, 83, 65, 95, 80]})
#
# group_all = pd.concat([group_a, group_b])
# print(group_all)