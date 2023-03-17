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
            cstID = sys.argv[1]
            result = sys.argv[2]
            
            resultSql = "UPDATE TB100023 SET WehagoBookMake='"+result+"' WHERE CSTID='"+cstID+"';"
            curs.execute(resultSql)
            conn.commit()
            
            if result == 'E' :
                log = sys.argv[3]
                logTime = sys.argv[4]
                logSql = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstID+"', 'WehagoBookMake', '"+log+"', '"+logTime+"');"
                curs.execute(logSql)
                conn.commit()
    finally:
        conn.close()
Result_Input()