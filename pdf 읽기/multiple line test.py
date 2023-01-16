import pdfplumber
from collections import namedtuple
import pandas as pd
import re
import os

Line = namedtuple('Line', 'title content detail')
title_re = re.compile(r'\d[.]')
date2_re = re.compile(r'\w\s\s\w')
only_content_re = re.compile(r'\s\w')

with pdfplumber.open('C:\\RPA\\TEST\\GHSMSDS\\GHSMSDS.pdf') as pdf:
    page_idx = 1

    print(len(pdf.pages))
    # page 만큼 반복
    for page in pdf.pages:
        data = []
        text = page.extract_text(x_tolerance=2, y_tolerance=0)     #tolerance : 허용 오차
        print(text)

        for line in text.split('\n'):
            line = line.strip()                 # 데이터 정제를 위해 trim

            if re.search(title_re, line):       # 타이틀 데이터
                data.append(['', '', ''])           # 한줄 넣기
                title = line
                content = ''
                detail = ''
            elif re.search(date2_re, line):     # 소제목, 내용 같이 있는 경우
                line = line.split('  ')
                title = line[0]
                content = line[1]
                if len(line) == 3:
                    detail = line[2]
                else:
                    detail = ''
            elif re.search(only_content_re, line):      # 내용만 있는 경우
                line = line.split('  ')
                title = ''
                content = line[0]
                if len(line) == 2:
                    detail = line[1]
                else:
                    detail = ''
            else:                               # 소제목만 있는 경우
                title = line
                content = ''
                detail = ''

            line_info = Line(title, content, detail)    # tuple 데이터에 내용 저장
            data.append(line_info)

        print(data)
        df = pd.DataFrame(data)

        # 엑셀에 저장
        if not os.path.exists('C:\\RPA\\TEST\\GHSMSDS\\GHSMSDS.xlsx'):
            with pd.ExcelWriter('C:\\RPA\\TEST\\GHSMSDS\\GHSMSDS.xlsx', mode='w', engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=str(page_idx))
        else:
            with pd.ExcelWriter('C:\\RPA\\TEST\\GHSMSDS\\GHSMSDS.xlsx', mode='a', engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=str(page_idx))

        page_idx += 1


