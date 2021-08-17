import pymysql

#배포용
config = {
    'database': 'rcm2000$user',
    'user': 'rcm2000',
    'password': 'mariadb11!!',
    'host':'rcm2000.mysql.pythonanywhere-services.com',
    'port': 3306,
    'charset':'utf8',
    'use_unicode':True
}


#로컬용
# config = {
#     'database': 'userdb',
#     'user': 'project02',
#     'password': '111111',
#     'host':'127.0.0.1',
#     'port': 3306,
#     'charset':'utf8',
#     'use_unicode':True
# }
class Db:
    def getConnection(self):
        conn = pymysql.connect(**config);
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            conn.close();