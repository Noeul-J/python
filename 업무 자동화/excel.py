import win32com.client
import time

# 엑셀 프로그램 실행
excel = win32com.client.Dispatch("Excel.Application")
# 실행된 엑셀의 시각화
excel.Visible = True
time.sleep(2)

# 새 파일 생성
wb = excel.Workbooks.Add()  # 엑셀파일(통합문서) 생성, Sheet1 자동생성
ws = wb.Worksheets('Sheet1')    # 시트 변수 지정

# # # 기존 파일 열기
# # wb = excel.Workbooks.Open('파일경로')
# # ws = wb.ActiveSheet # 활성화 시트 변수 지정

# 시트 추가
ws = excel.Worksheets.Add()
ws = wb.Worksheets.Add()
ws.Name = '새시트'
time.sleep(2)

# 시트 선택
wb.Worksheets('새시트').Select()
# excel.Worksheets('Sheet1').Select()
time.sleep(2)

# 시트 삭제
wb.Worksheets('Sheet1').Delete()

# 셀 row, col과 값 지정하여 값 넣기
