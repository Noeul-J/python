import pymysql
import os
import sys
import json
from datetime import datetime

#전체 Select
def DB_Data_Export():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            # t for Target, b for Basic Info, c for Current Info
            # "+str(datetime.now().year)+"
            targetSql = "SELECT t.CSTID, t.BIZ_ID, b.CSTNAME, IFNULL(b.MOBILE, ''), IFNULL(b.RESIDENT_ID, '') " \
                        "FROM TB100023 AS t " \
                        "LEFT JOIN TB100020 AS b ON t.CSTID=b.CSTID " \
                        "LEFT JOIN TB100022 AS a ON t.BIZ_ID=a.BIZ_ID " \
                        "WHERE IFNULL(t.HomeTaxPrint, '')='R' AND a.CST_TYPE_YEAR='2021' LIMIT 10;"
            curs.execute(targetSql)
            rs = curs.fetchall()
            
            if rs != None :
                for row in rs:
                    statusSql = "UPDATE TB100023 SET HomeTaxPrint='I' WHERE BIZ_ID='"+str(row[1])+"';"
                    curs.execute(statusSql)
                    
                conn.commit()
            return rs
    finally:
        conn.close()
result = DB_Data_Export()
json_str = json.dumps(result, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
print("<peon>")
print(json_str)
print("</peon>")
