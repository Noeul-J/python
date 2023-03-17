import pymysql
import os
import sys
import json
from datetime import datetime

def DB_Data_Export():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='db.sostax.kr', port=3306, user='sschina', passwd='shinseung1@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            # "+str(datetime.now().year)+"
            sql = "SELECT t.ID FROM TB100023 AS t " \
                  "LEFT JOIN TB100020 AS b ON t.CSTID=b.CSTID " \
                  "LEFT JOIN TB100022 AS a ON t.CSTID=a.CSTID " \
                  "WHERE IFNULL(t.HomeTaxPrint, '')='I' AND a.CST_TYPE_YEAR='2021';";
            print(sql)
            curs.execute(sql)
            rs = curs.fetchall()
            print(len(rs))
            if rs != None :
                for row in rs:
                    sql = "UPDATE TB100023 SET HomeTaxPrint='R' WHERE ID='"+str(row[0])+"';"
                    curs.execute(sql)
                    conn.commit()
    finally:
        conn.close()

DB_Data_Export()

