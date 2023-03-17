import pymysql
import os
import sys
import json
from datetime import datetime

#전체 Select
def Result_Input():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            cstId = sys.argv[1]
            bizId = sys.argv[2]
            result = sys.argv[3]
            regDate = sys.argv[4]
            
            resultQry = "UPDATE TB100023 SET ManualDown='"+result+"', ManualDown_REGDATE='"+regDate+"' WHERE BIZ_ID='"+bizId+"';"
            curs.execute(resultQry)
            conn.commit()
                
            if result == 'Y' :
                incomeTax = sys.argv[5]
                incomeReportNum = sys.argv[6]
                localTax = sys.argv[7]
                localReportNum = sys.argv[8]
                updateQry = "UPDATE TB100022 SET INCOME_TAX='"+incomeTax+"', REPORT_NUM_INCOME='"+incomeReportNum+"', JIBANG_TAX='"+localTax+"', REPORT_NUM_WETAX='"+localReportNum+"', REQ_DATE='"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' WHERE BIZ_ID='"+bizId+"';"
                curs.execute(updateQry)
                conn.commit()
            elif result == 'H':
                incomeTax = sys.argv[5]
                incomeReportNum = sys.argv[6]
                hReason = sys.argv[7]
                logTime = sys.argv[8]
                updateQry = "UPDATE TB100022 SET INCOME_TAX='"+incomeTax+"', REPORT_NUM_INCOME='"+incomeReportNum+"' WHERE BIZ_ID='"+bizId+"';"
                logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'ManualDown', '"+hReason+"', '"+logTime+"');"
                curs.execute(logQry)
                conn.commit()
            else :
                errReason = sys.argv[5]
                logTime = sys.argv[6]
                logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'HomeTaxUpload', '"+errReason+"', '"+logTime+"');"
                curs.execute(logQry)
                conn.commit()
    finally:
        conn.close()
Result_Input()
