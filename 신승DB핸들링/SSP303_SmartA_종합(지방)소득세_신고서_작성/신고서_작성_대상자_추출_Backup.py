import pymysql
import os
import sys
import json
from datetime import datetime

# tg : Target(TB100023)
# cst : Customer(TB100020)
# ad : AdditionalInfo(TB100022)
# cmp : Company(TB100030)
# rt : ReportType(TB300010)

def Get_Customer_To_Report():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    
    try:
        with conn.cursor() as curs:
            branches = "'강남','세무톡'"
            targetSql = "SELECT tg.CSTID, cst.CSTNAME, cst.RESIDENT_ID, cmp.DOUZONE_SVR, cmp.DOUZONE_CODE, rt.DUTY_TYPE, rt.EXP_RATIO FROM TB100023 AS tg LEFT JOIN TB100020 AS cst ON tg.CSTID=cst.CSTID LEFT JOIN TB100022 AS ad ON tg.CSTID=ad.CSTID LEFT JOIN TB100030 AS cmp ON tg.CSTID=cmp.CSTID LEFT JOIN TB300010 AS rt ON tg.CSTID=rt.CSTID WHERE IFNULL(tg.SmartABookMake, '')='R' AND ad.CST_TYPE_YEAR='2021' AND IFNULL(CODE_TO_STR(ad.REG_BRANCH), '') IN ("+branches+") LIMIT 10;"
            #"+str(datetime.now().year)+"
            curs.execute(targetSql)
            tgRow = curs.fetchone()
            print(tgRow)
            if tgRow != None :
                tgCstId = tgRow[0]
                statusSql = "UPDATE TB100023 SET SmartABookMake='I' WHERE CSTID='"+str(tgCstId)+"';"
                curs.execute(statusSql)
                conn.commit()
                
                totalIncomeSql = "SELECT SEC_CODE, AMOUNT_PAID, SIM_RATIO_N, SIM_RATIO_S FROM TB300020 WHERE CST_TYPE_YEAR='2021' AND CSTID='"+str(tgCstId)+"';"
                curs.execute(totalIncomeSql)
                tiRows = curs.fetchall()
                
                otherBizSql = "SELECT * FROM TB300030 WHERE CST_TYPE_YEAR='2021' AND CSTID='"+str(tgCstId)+"';"
                curs.execute(otherBizSql)
                otherBizRows = curs.fetchone()
                
                deductionSql = "SELECT EXI_TAX, NPIP, PERSON_SAVE, SMALL_BIZ_DED, RET_SAVE, PEN_SAVE FROM TB300031 WHERE CST_TYPE_YEAR='2021' AND CSTID='"+str(tgCstId)+"';"
                curs.execute(deductionSql)
                dedRows = curs.fetchone()
                
                famSql = "SELECT RELATION, FAM_NAME, RESIDENT_ID, DISORDER, WOMAN, SINGLE_PARENT FROM TB310040 WHERE CSTID='"+str(tgCstId)+"';"
                curs.execute(famSql)
                famRows = curs.fetchall()
                
                paySql = "SELECT BIZ_NUM, COMP_NAME, INCOME_TAX FROM TB310030 WHERE CSTID='"+str(tgCstId)+"';"
                curs.execute(paySql)
                payRows = curs.fetchall()
                
                tgRowJson = json.dumps(tgRow, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                tiRowJson = json.dumps(tiRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                otherBizRowJson = json.dumps(otherBizRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                dedRowJson = json.dumps(dedRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                famRowJson = json.dumps(famRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                payRowJson = json.dumps(payRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
                resultDict = {'tg':tgRowJson, 'ti':tiRowJson, 'ob':otherBizRowJson, 'ded':dedRowJson, 'fam':famRowJson, 'pay':payRowJson}
                return resultDict
            else :
                return None
    finally:
        conn.close()
        
resultDict = Get_Customer_To_Report()

print("<peon>")
print(resultDict)
print("</peon>")

