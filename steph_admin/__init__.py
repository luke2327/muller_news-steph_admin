import pymysql.cursors
class Database():
    connection = None
    def connect_db(self):
        import os
        try :
            if os.uname()[1] == 'ip-172-31-31-7':  # Dev Server
                PHOST = 'localhost'
            elif os.uname()[1] == 'ip-172-31-31-67':
                PHOST = 'ip-172-31-31-7'

        except Exception as e :
            PHOST = 'admin.swips.co'
        self.connection = pymysql.connect(host=PHOST,
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
