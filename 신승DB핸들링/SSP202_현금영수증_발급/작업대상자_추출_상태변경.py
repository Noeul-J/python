import pymysql
import os
import sys
import json

#전체 Select
def DB_Data_Export():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            targetSql = "SELECT tg.CSTID, tg.BIZ_ID, IFNULL(ad.DEP_FEE, ''), IFNULL(cst.RESIDENT_ID, ''), IFNULL(cst.MOBILE, '') FROM TB100023 AS tg LEFT JOIN TB100020 AS cst ON tg.CSTID=cst.CSTID LEFT JOIN TB100022 AS ad ON tg.BIZ_ID=ad.BIZ_ID WHERE IFNULL(tg.CashReport, '')='R' LIMIT 10;"
            curs.execute(targetSql)
            rs = curs.fetchall()
            
            if rs != None :
                for row in rs:
                    tgBizId = row[1]
                    statusSql = "UPDATE TB100023 SET CashReport='I' WHERE BIZ_ID='"+str(tgBizId)+"';"
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
