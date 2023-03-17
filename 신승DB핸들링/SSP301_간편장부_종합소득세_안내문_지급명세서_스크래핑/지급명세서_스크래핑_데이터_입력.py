import pymysql
import os
import sys
import json
from datetime import datetime

##  TB310030 테이블(지급명세서 스크래핑)에 스크래핑 데이터 insert
def insertTB310030() :
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    try:
        # Table 결과 SELECT
        with conn.cursor() as curs:
            insertSql = sys.argv[1]                                
            print(insertSql)
            curs.execute(insertSql)
            curs.fetchone()
            conn.commit()
            print("Query Execution Completed")
        result = True
    except :
        result = False
    finally:
        conn.close()
        return result

def main():
    result = insertTB310030()
    print("<peon>")
    print(result)
    print("</peon>")

if __name__ == "__main__":
	main()