import pymysql
import os
import sys
import json
import datetime

#전체 수임등록 작업결과, 에러로그 입력
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
            
            statusSql = "UPDATE TB100023 SET HomeTaxConsignment='"+result+"', HomeTaxConsignment_REGDATE='"+regDate+"' WHERE BIZ_ID='"+bizId+"';"
            curs.execute(statusSql)
            conn.commit()
            
            if result == 'E' :
                errReason = sys.argv[5]
                logTime = sys.argv[6]
                logSql = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES ('"+cstId+"', 'HomeTaxConsignment', '"+errReason+"', '"+logTime+"');"
                curs.execute(logSql)
                conn.commit()
            print("작업결과 입력 완료")
    finally:
        conn.close()
Result_Input()