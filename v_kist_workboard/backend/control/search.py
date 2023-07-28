from model.db import conn_mysqldb


class PRC_LKP():
    @staticmethod
    def sch_rpa(startDt, endDt, prc_name):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        
        if prc_name == "전체":
            print("전체 조회")
            
            sql = "SELECT a.PROCESS_NM, b.* " + \
                "FROM process_name a LEFT JOIN process_result b ON a.PROCESS_ID = b.PROCESS_ID " + \
                "where DATE_FORMAT(b.rundate,'%Y-%m-%d') BETWEEN '" + str(startDt) + "' " + \
                "and '" + str(endDt) + "' "
            
        else:
            print(f"{prc_name} 조회")
            sql = "SELECT a.PROCESS_NM, b.* " + \
                  "FROM process_name a LEFT JOIN process_result b ON a.PROCESS_ID = b.PROCESS_ID " + \
                  "where DATE_FORMAT(b.rundate,'%Y-%m-%d') BETWEEN '" + str(startDt) + "' " + \
                  "and '" + str(endDt) + "' "+ \
                  "and b.PROCESS_ID = '"+ str(prc_name) +"' " + \
                  "and a.PROCESS_ID = '"+ str(prc_name) +"'"
                  
        db_cursor.execute(sql)
        result = db_cursor.fetchall()
        if not result:
            return None
        else:
            return result
    