from mysql.connector import Error
from src.database.connection import Connection
from src.logs.message import logError, logSuccess


class CreateStudent:
    def __init__(self, data):
        self.connection = Connection()
        self.email = data['email']
        self.name = data['name']
        self.username = data['username']
        self.password = data['password']

    def execute(self):
        try: 
            self.connection.connect()
            sql = '''
                select * from tbl_student where email = %s
            '''
            result = self.connection.query(sql, (self.email,)).fetchone()
            if (result): return logError("Student already exists", 400)

            sql = '''
                insert into tbl_student 
                (name, username, email, password) values (%s, %s, %s)
            '''
            parameters = (
                self.name,
                self.username,
                self.email,
                self.password,
            )
            self.connection.query(sql, (parameters))
            self.connection.commit()
            return logSuccess("Student created", 200)
        except Error as error: raise Exception(error)
        finally: self.connection.close()

        