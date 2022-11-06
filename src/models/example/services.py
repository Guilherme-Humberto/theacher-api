from mysql.connector import Error
from src.database.connection import Connection


class Example:
    def __init__(self):
        self.connection = Connection()

    ## LIST AUTHORS
    def listAll(self):
        try: 
            return 'return all examples'
        except Error as error: raise Exception(error)
        finally: self.connection.close()