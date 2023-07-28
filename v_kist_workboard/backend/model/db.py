import pymysql

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306

# MYSQL_HOST = '161.122.37.174'
# MYSQL_PORT = 13307

MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user='kist',
    passwd='kist',
    db='kist',
    charset='utf8'
)


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
