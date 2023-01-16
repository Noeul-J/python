import re

content_re = re.compile(r'\w\s\s\w')
content = re.search(content_re, '안녕하세요  소화수의 처분을 위해 도랑을 파서 가두고 물질이 흩어지지 않게 하시오 ')
if content:
    print('야호')