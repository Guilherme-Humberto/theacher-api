from mysql.connector import Error
from src.database.connection import Connection


class Category:
    def __init__(self):
        self.connection = Connection()

    ## LIST CATEGORIES
    def listAll(self):
        try: 
            self.connection.connect()
            sql = '''
                select * from category order by title
            '''
            return self.connection.query(sql).fetchall()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## GET CATEGORY BY ID
    def get(self, categoryId):
        try: 
            self.connection.connect()
            sql = '''
                select * from category where id = %s
            '''
            result = self.connection.query(sql, (categoryId,))
            return result.fetchone()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## CREATE NEW CATEGORY
    def create(self, objData):
        try: 
            self.connection.connect()
            sql = '''
                insert into category (id, title) values (null, %s)
            '''
            data = ( objData['title'], )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.listAll()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## UPDATE CATEGORY
    def update(self, categoryId, objData):
        try: 
            if not categoryId: return 'Id is required'
            
            self.connection.connect()
            sql = ''' 
                update category set title = %s where id = %s 
            '''
            data = ( objData['title'], categoryId )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.get(categoryId)
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    ## DELETE CATEGORY
    def delete(self, categoryId):
        try: 
            self.connection.connect()
            sql = ''' delete from category where id = %s '''
            self.connection.query(sql, (categoryId,))
            self.connection.commit()
        except Error as error: raise Exception(error)
        finally: self.connection.close()