from mysql.connector import Error
from src.database.connection import Connection
from src.logs.message import logError


class GetStudent:
    def __init__(self, data):
        self.connection = Connection()
        self.username = data['username']
        self.password = data['password']

    def execute(self):
        try: 
            self.connection.connect()
            sql = '''
                select * from tbl_student where username = %s and password = %s
            '''
            result = self.connection.query(sql, (self.username, self.password,)).fetchone()
            if (not result): return logError("Student not found", 400)
            return result
        except Error as error: raise Exception(error)
        finally: self.connection.close()