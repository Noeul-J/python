import pymysql
import os
import sys
import json
import win32com.client as win32 #pip install pywin32

# DB 연결 및 DATA Insert
def insert_func(paymentList):
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:

            insertSql = """insert into TB310010
                            values(0, %(publish_flag)s, %(sales_date)s, %(supply_value)s, %(vat_value)s, %(service_value)s, %(total_value)s, %(commit_num)s, %(iss_method)s, %(trade_flag)s, %(memo)s, now());"""
            deleteSql = """DELETE FROM TB310010
                            WHERE date_format(regdate, "%Y-%m-%d") = CURDATE();"""
            
            curs.execute(deleteSql)
            curs.executemany(insertSql, paymentList)
            conn.commit()
            print(curs.rowcount, "개의 레코드가 입력되었습니다.")
    finally:
        conn.close()

# 엑셀에서 데이터 추출
def extract_data():
    try:
        excelFilepath = sys.argv[1]
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = False
        wb = excel.Workbooks.Open(excelFilepath)

        sheet = wb.Worksheets(1)
        lastRow = sheet.UsedRange.Rows.Count
        
        paymentList = list()
        # 3행부터 데이터 있음
        for i in range(3, lastRow+1) :
            publish = sheet.Cells(i, 1).Value       # 발행구분
            sales_date = sheet.Cells(i, 2).Value    # 매출일시
            supply = int(sheet.Cells(i, 3).Value)   # 공급가액
            vat = int(sheet.Cells(i, 4).Value)      # 부가세
            service = int(sheet.Cells(i, 5).Value)  # 봉사료
            total = int(sheet.Cells(i, 6).Value)    # 총금액
            commit = sheet.Cells(i, 7).Value        # 승인번호
            iss = sheet.Cells(i, 8).Value           # 발급수단
            trade = sheet.Cells(i, 9).Value         # 거래구분
            memo = sheet.Cells(i, 10).Value         # 비고

            dic = {'publish_flag':publish, 'sales_date':sales_date, 'supply_value':supply, 'vat_value':vat,
                    'service_value':service, 'total_value':total, 'commit_num':commit, 'iss_method':iss, 'trade_flag':trade, 'memo':memo}
            paymentList.append(dic)

        insert_func(paymentList)

    except Exception as e:
        print(e)
    finally:
        # 엑셀 종료
        excel.Quit()  

extract_data()