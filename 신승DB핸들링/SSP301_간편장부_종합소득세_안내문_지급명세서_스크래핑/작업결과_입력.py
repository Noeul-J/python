import pymysql
import os
import sys
import json

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
            
            resultSql = "UPDATE TB100023 SET HomeTaxPrint='"+result+"', HomeTaxPrint_REGDATE='"+regDate+"' WHERE BIZ_ID='"+bizId+"';"
            curs.execute(resultSql)
            conn.commit()
            
            if result == 'Y' :
                fileCount = sys.argv[5]
                fileCountSql = "INSERT INTO TB100022 (BIZ_ID, FILE_COUNT) VALUES ('"+bizId+"', '"+fileCount+"') ON DUPLICATE KEY UPDATE FILE_COUNT='"+fileCount+"';"
                curs.execute(fileCountSql)
                conn.commit()
            elif result == 'H' :
                fileCount = sys.argv[5]
                log = sys.argv[6]
                logTime = sys.argv[7]
                fileCountSql = "INSERT INTO TB100022 (BIZ_ID, FILE_COUNT) VALUES ('"+bizId+"', '"+fileCount+"') ON DUPLICATE KEY UPDATE FILE_COUNT='"+fileCount+"';"
                curs.execute(fileCountSql)
                logSql = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'HomeTaxPrint', '"+log+"', '"+logTime+"');"
                curs.execute(logSql)
                conn.commit()
            else :
                log = sys.argv[5]
                logTime = sys.argv[6]
                logSql = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'HomeTaxPrint', '"+log+"', '"+logTime+"');"
                curs.execute(logSql)
                conn.commit()
    finally:
        conn.close()
Result_Input()