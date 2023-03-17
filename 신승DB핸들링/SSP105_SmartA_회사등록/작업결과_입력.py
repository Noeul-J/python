import pymysql
import os
import sys
import json

def Result_Input():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            rowId = sys.argv[1]
            result = sys.argv[2]
            
            resultQry = "UPDATE TB100023 SET CompRegCheck='"+result+"' WHERE ID='"+rowId+"';"
            curs.execute(resultQry)
            conn.commit()
            
            if result == 'E' :
                errReason = sys.argv[3]
                logDate = sys.argv[4]
                logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ((SELECT CSTID FROM TB100023 WHERE ID='"+rowId+"'), 'CompRegCheck', '"+errReason+"', '"+logDate+"');"
                curs.execute(logQry)
                conn.commit()
            else :
                server = sys.argv[3]
                compCode = sys.argv[4]
                compCodeQry = "UPDATE TB100030 SET DOUZONE_SVR='"+server+"', DOUZONE_CODE='"+compCode+"' WHERE CSTID=(SELECT CSTID FROM TB100023 WHERE ID='"+rowId+"');"
                curs.execute(compCodeQry)
                conn.commit()
            print("작업결과 입력 완료")
    finally:
        conn.close()
Result_Input()