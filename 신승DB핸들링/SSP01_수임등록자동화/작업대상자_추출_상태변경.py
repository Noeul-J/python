import pymysql
import os
import sys
import json
from datetime import datetime

# TB100023 Table의 작업 대상 중 HometaxConsignment 컬럼의 값이 R이며,
# TB100023, TB100020, TB100022 의 CSTID 값이 같은 한 Row를 Select
# Select한 결과 한 Row의 상태를 R(Reserved) -> I(In-Progress) 변경
def GetTargetCstAndUpdateStatus():
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:        
        with conn.cursor() as curs:
            # "+str(datetime.now().year)+"
            sql = "SELECT t.CSTID, t.BIZ_ID, IFNULL(b.CSTNAME, ''), IFNULL(b.MOBILE, ''), IFNULL(b.RESIDENT_ID, ''), IFNULL(c.BIZ_NUM, '') FROM TB100023 AS t LEFT JOIN TB100020 AS b ON t.CSTID=b.CSTID LEFT JOIN TB100022 AS a ON t.BIZ_ID=a.BIZ_ID LEFT JOIN TB100030 AS c ON t.BIZ_ID=c.BIZ_ID WHERE IFNULL(a.REG_BRANCH, '')<>'' AND IFNULL(t.HomeTaxConsignment, '')='R' AND a.CST_TYPE_YEAR='2021' LIMIT 10;"
            print(sql)
            curs.execute(sql)
            rs = curs.fetchall()
            
            if rs != None :
                for row in rs:
                    sql = "UPDATE TB100023 SET HometaxConsignment='I' WHERE BIZ_ID='"+str(row[1])+"';"
                    print(sql)
                    curs.execute(sql)
                    conn.commit()
                    
            return rs
    finally:
        conn.close()
result = GetTargetCstAndUpdateStatus()
json_str = json.dumps(result, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
print("<peon>")
print(json_str)
print("</peon>")