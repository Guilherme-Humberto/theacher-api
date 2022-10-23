from mysql.connector import Error
from src.database.connection import Connection


class Author:
    def __init__(self):
        self.connection = Connection()

    ## LIST AUTHORS
    def listAll(self):
        try: 
            self.connection.connect()
            sql = '''
                SELECT * FROM author order by first_name
            '''
            return self.connection.query(sql).fetchall()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## GET AUTHOR BY ID
    def get(self, authorId):
        try: 
            self.connection.connect()
            sql = '''SELECT * FROM author where id = %s'''
            result = self.connection.query(sql, (authorId,))
            return result.fetchone()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## CREATE NEW AUTHOR
    def create(self, objData):
        try: 
            self.connection.connect()
            sql = '''
                insert into author (id, first_name, second_name, email) 
                values (null, %s, %s, %s)
            '''
            data = (
                objData['first_name'], 
                objData['second_name'], 
                objData['email']
            )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.listAll()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## DELETE AUTHOR BY ID
    def delete(self, authorId):
        try: 
            self.connection.connect()
            sql = ''' delete from author where id = %s '''
            self.connection.query(sql, (authorId,))
            self.connection.commit()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## UPDATE AUTHOR
    def update(self, authorId, objData):
        try: 
            if not authorId: return 'Id obrigatório'

            self.connection.connect()
            sql = ''' 
                update author set first_name = %s,
                second_name = %s, email = %s
                where id = %s 
            '''
            data = (
                objData['first_name'], 
                objData['second_name'], 
                objData['email'],
                authorId
            )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.get(authorId)
        except Error as error: raise Exception(error)
        finally: self.connection.close()