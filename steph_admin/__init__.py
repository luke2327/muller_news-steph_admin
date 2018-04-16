import pymysql.cursors
class Database():
    connection = None
    def connect_db(self):
        self.connection = pymysql.connect(host='admin.swips.co',
             user='stephen',
             password='20150821',
             db='spocosy',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor)

    def disconnect_db(self):
        self.connection.close()

    def get_data(self, sql):
        self.connect_db()
        try :
            with self.connection.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally :
            self.disconnect_db()

    def insert_data(self, sql):
        self.connect_db()
        try :
            with self.connection.cursor() as cursor:
                # Read a single record
                result = cursor.execute(sql)
                self.connection.commit()
                return result
        except Exception as e :
            print(e)
            return -1
        finally :
            self.disconnect_db()
