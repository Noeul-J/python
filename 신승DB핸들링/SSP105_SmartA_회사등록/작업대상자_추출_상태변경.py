import pymysql
import os
import sys
import json
from datetime import datetime

def DB_Data_Export():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            # t for Target, b for Basic Data, a for Additional Data, c for Company
            targetQry = "SELECT t.ID, b.CSTNAME, b.MOBILE, b.RESIDENT_ID, b.SECTOR_CODE, CODE_TO_STR(a.REG_BRANCH), c.COMPANY, IFNULL(c.BIZ_NUM, ''), c.ADDRESS_LOAD FROM TB100023 AS t LEFT JOIN TB100020 AS b ON t.CSTID=b.CSTID LEFT JOIN TB100022 AS a ON t.BIZ_ID=a.BIZ_ID LEFT JOIN TB100030 AS c ON t.BIZ_ID=c.BIZ_ID AND t.CSTID=c.CSTID WHERE t.CompRegCheck='R' AND a.CST_TYPE_YEAR='"+str(datetime.now().year)+"';"
            curs.execute(targetQry)
            rs = curs.fetchall()
            
            if rs != None :
                for row in rs :
                    updateQry = "UPDATE TB100023 SET CompRegCheck='I' WHERE ID='"+str(row[0])+"';"
                    curs.execute(updateQry)
                    
                conn.commit()
            return rs
    finally:
        conn.close()
result = DB_Data_Export()
json_str = json.dumps(result, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
print("<peon>")
print(json_str)
print("</peon>")