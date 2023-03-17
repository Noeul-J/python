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
            
            resultQry = "UPDATE TB100023 SET SmartAToConvert='"+result+"', SmartAToConvert_REGDATE='"+regDate+"' WHERE BIZ_ID='"+bizId+"';"
            curs.execute(resultQry)
            conn.commit()
            
            if result == 'Y' :
                updQry = "UPDATE TB100023 SET HomeTaxUpload='R' WHERE BIZ_ID='"+bizId+"';"
                curs.execute(updQry)
                conn.commit()
            elif result == 'E' :         
                errReason = sys.argv[5]
                logDate = sys.argv[6]
                logQry = "INSERT INTO TB700020 (CSTID, STEP_NAME, LOG, LOG_TIME) VALUES('"+cstId+"', 'SmartAToConvert', '"+errReason+"', '"+logDate+"');"
                curs.execute(logQry)
                conn.commit()
            
            print("작업결과 입력 완료")
    finally:
        conn.close()
Result_Input()
