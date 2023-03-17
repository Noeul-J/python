import pymysql
import os
import sys

##  TB310030 테이블(지급명세서 스크래핑)에 스크래핑 데이터 전 중복데이터 삭제
def RemoveDuplicate() :
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    try:
        with conn.cursor() as curs:
            cstId = sys.argv[1]
            bizNum = sys.argv[2]
            attrYear = sys.argv[3]
            
            selectQuery = "SELECT ID FROM TB310030 WHERE CSTID='"+cstId+"' AND BIZ_NUM='"+bizNum+"' AND INCOME_ATTR_YEAR='"+attrYear+"';"
            curs.execute(selectQuery)
            rs = curs.fetchall()
            
            if rs != None :
                for row in rs :
                    rowId = str(row[0])
                    deleteQuery = "DELETE FROM TB310030 WHERE ID='"+rowId+"';"
                    curs.execute(deleteQuery)
                conn.commit()
            print("Query Execution Completed")
        result = True
    except Exception as ex:
        print(ex)
        result = False
    finally:
        conn.close()
        return result

def main():
    result = RemoveDuplicate()
    print("<peon>")
    print(result)
    print("</peon>")

if __name__ == "__main__":
	main()