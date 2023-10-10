# https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# pip install JPype1-1.1.2-cp39-cp39-win_amd64.whl
# pip install konlpy
# pip uninstall jpype1
# pip install jpype1

from konlpy.tag import Okt
import konlpy
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

moon = open('speech_moon.txt', encoding='UTF-8').read()
moon = re.sub('[^가-힣]', ' ', moon)
hannanum = konlpy.tag.Hannanum()

# 명사 추출하기
nouns = hannanum.nouns(moon)

df_word = pd.DataFrame({'word': nouns})
# print(df_word)

# 글자 수
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count >= 2')

# 단어 빈도 그래프 만들기
df_word = df_word.groupby('word', as_index=False)\
                 .agg(n=('word', 'count'))\
                 .sort_values('n', ascending=False)
# print(df_word)

top20 = df_word.head(20)

# plt.rcParams.update({'font.family'    : 'Malgun Gothic',  # 한글 폰트 설정
#                      'figure.dpi'     : '120',            # 해상도 설정
#                      'figure.figsize' : [6.5, 6]})        # 가로 세로 크기 설정
# sns.barplot(data=top20, y='word', x='n')
# plt.show()

# [워드 클라우드 만들기]
font = 'DoHyeon-Regular.ttf'

dic_word = df_word.set_index('word').to_dict()['n']

wc = WordCloud(random_state=1234,
               font_path = font,
               width = 400,
               height = 400,
               background_color ='white')

img_wordcloud = wc.generate_from_frequencies(dic_word)

plt.figure(figsize = (10, 10))      # 가로, 세로 크기 설정
plt.axis('off')                     # 테두리 선 없애기
plt.imshow(img_wordcloud)           # 워드 클라우드 출력


