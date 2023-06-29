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
            reportId = sys.argv[5]
            
            # resultQry = "UPDATE TB100023 SET HomeTaxUpload='"+result+"', HomeTaxUpload_REGDATE='"+regDate+"', HT_REPORT_ID='"+reportId+"' WHERE BIZ_ID='"+bizId+"';"
            # curs.execute(resultQry)
            # conn.commit()
            #
            # if result == 'Y' :
            #     incomeTax = sys.argv[6]
            #     incomeReportNum = sys.argv[7]
            #     localTax = sys.argv[8]
            #     localReportNum = sys.argv[9]
            #     updateQry = "UPDATE TB100022 SET INCOME_TAX='"+incomeTax+"', REPORT_NUM_INCOME='"+incomeReportNum+"', JIBANG_TAX='"+localTax+"', REPORT_NUM_WETAX='"+localReportNum+"', REQ_DATE='"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' WHERE BIZ_ID='"+bizId+"';"
            #     curs.execute(updateQry)
            #     conn.commit()
            # else :
            #     errReason = sys.argv[6]
            #     logTime = sys.argv[7]
            #     logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'HomeTaxUpload', '"+errReason+"', '"+logTime+"');"
            #     curs.execute(logQry)
            #     conn.commit()
    finally:
        conn.close()
Result_Input()
