import pymysql

db_conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'kist',
    db = 'blog',
    charset='utf8'
)

user_db = db_conn.cursor()

sql = """
select * from user_info
"""
user_db.execute(sql)
# db_conn.commit()
results = user_db.fetchall()
for result in results:
    print(result, type(result))
    
    
user_db.close()
