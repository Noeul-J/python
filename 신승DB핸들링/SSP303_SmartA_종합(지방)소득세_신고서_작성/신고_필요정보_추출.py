import pymysql
import os
import sys
import json
from datetime import datetime

# cst : Customer(TB100020)
# ad : AdditionalInfo(TB100022)
# cmp : Company(TB100030)
# rt : ReportType(TB300010)

def Get_Report_Information():
    print("mysql Connection 진행")
    conn = pymysql.connect(host='182.162.143.216', port=3306, user='sschina', passwd='Andy4240!@', db='dbsschina', charset='utf8')
    print("mysql Connection 완료")
    
    try:
        with conn.cursor() as curs:
            tgCstId = sys.argv[1]
            tgBizId = sys.argv[2]
            
            #"+str(datetime.now().year)+"
            totalIncomeSql = "SELECT IFNULL(BIZ_NUM, ''), IFNULL(SEC_CODE, ''), IFNULL(AMOUNT_PAID, 0), " \
                             "IFNULL(SIM_RATIO_N, 0), IFNULL(SIM_RATIO_S, 0) FROM TB300020 WHERE CST_TYPE_YEAR='2021' AND BIZ_ID='"+str(tgBizId)+"';"
            curs.execute(totalIncomeSql)
            tiRows = curs.fetchall()
            
            otherBizSql = "SELECT * FROM TB300030 WHERE CST_TYPE_YEAR='2021' AND CSTID='"+str(tgCstId)+"';"
            curs.execute(otherBizSql)
            otherBizRows = curs.fetchone()
            
            deductionSql = "SELECT EXI_TAX, NPIP, PERSON_SAVE, SMALL_BIZ_DED, RET_SAVE, PEN_SAVE FROM TB300031 WHERE CST_TYPE_YEAR='2021' AND CSTID='"+str(tgCstId)+"';"
            curs.execute(deductionSql)
            dedRows = curs.fetchone()
            
            famSql = "SELECT RELATION, FAM_NAME, RESIDENT_ID, DISORDER, WOMAN, SINGLE_PARENT FROM TB310040 WHERE IFNULL(RELATION, '')<>'' AND BIZ_ID='"+str(tgBizId)+"';"
            curs.execute(famSql)
            famRows = curs.fetchall()
            
            paySql = "SELECT BIZ_NUM, COMP_NAME, INCOME_TAX FROM TB310030 WHERE BIZ_ID='"+str(tgBizId)+"' AND INCOME_ATTR_YEAR='2021';"
            curs.execute(paySql)
            payRows = curs.fetchall()
            
            tiRowJson = json.dumps(tiRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
            otherBizRowJson = json.dumps(otherBizRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
            dedRowJson = json.dumps(dedRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
            famRowJson = json.dumps(famRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
            payRowJson = json.dumps(payRows, ensure_ascii=False).encode('cp949',errors = 'replace').decode('cp949')
            resultDict = {'ti':tiRowJson, 'ob':otherBizRowJson, 'ded':dedRowJson, 'fam':famRowJson, 'pay':payRowJson}
            
            return resultDict
    finally:
        conn.close()
        
resultDict = Get_Report_Information()

print("<peon>")
print(resultDict)
print("</peon>")

