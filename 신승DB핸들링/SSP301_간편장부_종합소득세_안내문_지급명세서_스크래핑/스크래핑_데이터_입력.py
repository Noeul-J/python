import pymysql
import os
import sys
import json

#Table Select 결과에 따라 데이터 INSERT 혹은 UPDATE.
def sql_Send():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    try:
        # Table 결과 SELECT
        with conn.cursor() as curs:
            if len(sys.argv) == 4 :
                selectSql = sys.argv[1]
                insertSql = sys.argv[2]
                updateSql = sys.argv[3]
                
                print(selectSql)
                curs.execute(selectSql)
                curs.fetchone()
                rs = curs.rowcount
                
                # Select 결과 Row가 이미 있는 경우 Update
                if rs > 0 :
                    curs.execute(updateSql)
                    print(updateSql)
                else :
                    curs.execute(insertSql)
                    print(insertSql)
            
            elif len(sys.argv) == 2 :
                dupSql = sys.argv[1]
                print(dupSql)
                curs.execute(dupSql)
                    
            conn.commit()
            print("Query Execution Completed")
    finally:
        conn.close()
sql_Send()