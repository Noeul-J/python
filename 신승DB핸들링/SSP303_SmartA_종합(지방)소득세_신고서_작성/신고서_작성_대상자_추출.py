import pymysql
import os
import sys
import json
from datetime import datetime

def Get_Customer_To_Report():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    
    try:
        with conn.cursor() as curs:
            branches = "'강남','세무톡'"
            targetSql = "SELECT tg.CSTID, tg.BIZ_ID, cst.CSTNAME, IFNULL(cst.RESIDENT_ID, ''), " \
                        "IFNULL(ad.USER_RATIO, ''), IFNULL(cmp.DOUZONE_SVR, ''), IFNULL(cmp.DOUZONE_CODE, ''), IFNULL(rt.DUTY_TYPE, ''), " \
                        "IFNULL(rt.EXP_RATIO, ''), IFNULL(cst.REF_BANK, ''), IFNULL(cst.REF_ACC, '') " \
                        "FROM TB100023 AS tg " \
                        "LEFT JOIN TB100020 AS cst ON tg.CSTID=cst.CSTID " \
                        "LEFT JOIN TB100022 AS ad ON tg.BIZ_ID=ad.BIZ_ID " \
                        "LEFT JOIN TB100030 AS cmp ON tg.BIZ_ID=cmp.BIZ_ID " \
                        "LEFT JOIN TB300010 AS rt ON tg.CSTID=rt.CSTID " \
                        "WHERE IFNULL(tg.HomeTaxPrint, '')='Y' AND IFNULL(tg.SmartABookMake, '')='R' " \
                        "AND ad.CST_TYPE_YEAR = 2021 AND ad.CST_TYPE='A1001' LIMIT 1;"
            #"+str(datetime.now().year)+"
            curs.execute(targetSql)
            rs = curs.fetchall()
            
            # if rs != None :
            #     for row in rs:
            #         tgBizId = row[1]
            #         statusSql = "UPDATE TB100023 SET SmartABookMake='I' WHERE BIZ_ID='"+str(tgBizId)+"';"
            #         curs.execute(statusSql)
            #
            #     conn.commit()
            return rs
    finally:
        conn.close()
        
result = Get_Customer_To_Report()
json_str = json.dumps(result, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')

print("<peon>")
print(json_str)
print("</peon>")

