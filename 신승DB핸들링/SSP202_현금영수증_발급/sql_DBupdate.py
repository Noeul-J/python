import pymysql
import os
import sys

# DB 연결 및 DATA Insert
def update_func():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            cstID = sys.argv[1]
            bizId = sys.argv[2]
            result = sys.argv[3]
            regDate = sys.argv[4]
            updateSql = "UPDATE TB100023 SET CashReport='"+status+"', 'CashReport_REGDATE='"+regDate+"' WHERE BIZ_ID="+bizId+";"
            
            if status == "Y" :
                # 현금영수증 발급 완료 -> 승인번호, 발급일 입력
                appNum = sys.argv[5]
                issuedDate = sys.argv[6]
                insertSql = "INSERT INTO TB100022 (BIZ_ID, CSTID, CASH_REPORT_APP_NUM, CASH_REPORT_REGDATE) VALUES('"+bizId+ "', '" + cstID + "', '"+ aprvNum + "', '" + issuedDate + "') ON DUPLICATE KEY UPDATE CASH_REPORT_APP_NUM='"+aprvNum+"', CASH_REPORT_REGDATE='"+issuedDate+"'"
                curs.execute(insertSql)
            elif status == "E" :
                # 에러발생시 로그테이블에 로그남기기
                reason = sys.argv[5]
                logDate = sys.argv[6]
                logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES('"+cstId+"', 'SmartAToConvert', '"+reason+"', '"+logDate+"');"
                curs.execute(logQry)
            
            curs.execute(updateSql)
            conn.commit()
        
    finally:
        conn.close()

update_func()
