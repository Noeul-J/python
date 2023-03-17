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
            sql = """SELECT TB100023.cstid, TB100023.biz_id, dep_fee, mobile
                    FROM TB100023 LEFT JOIN TB100022
                                    ON TB100023.cstid = TB100022.cstid
                                    AND TB100023.biz_id = TB100022.biz_id
                                  LEFT JOIN TB100020
                                    ON TB100023.cstid = TB100020.cstid
                    WHERE CashReport = 'R';"""
            curs.execute(sql)
            rs = curs.fetchall()
            return rs
    finally:
        conn.close()

result = DB_Data_Export()
json_str = json.dumps(result, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
print("<peon>")
print(json_str)
print("</peon>")
