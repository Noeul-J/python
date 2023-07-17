import pymysql

db_conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'kist',
    passwd = 'kist',
    db = 'kist',
    charset='utf8'
)

user_db = db_conn.cursor()

sql = """select * from process_name"""
user_db.execute(sql)
results = user_db.fetchall()
for result in results:
    print(result, type(result))
