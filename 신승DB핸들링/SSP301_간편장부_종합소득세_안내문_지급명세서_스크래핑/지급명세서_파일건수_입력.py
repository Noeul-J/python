import pymysql
import os
import sys
import json

def Payment_FileCount_Input():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        with conn.cursor() as curs:
            bizId = sys.argv[1]
            fileCount = sys.argv[2]
            
            resultSql = "INSERT INTO TB100022 (BIZ_ID, FILE_COUNT) VALUES ('"+bizId+"', '"+fileCount+"') ON DUPLICATE KEY UPDATE FILE_COUNT='"+fileCount+"';"
            print(resultSql)
            curs.execute(resultSql)
            conn.commit()
    finally:
        conn.close()
Payment_FileCount_Input()