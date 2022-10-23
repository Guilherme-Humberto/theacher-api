from mysql.connector import Error
from src.models.authors.services import Author
from src.database.connection import Connection
from src.models.categories.services import Category


class Book:
    def __init__(self):
        self.connection = Connection()
        self.author = Author()
        self.category = Category()
    
    def listAll(self):
        try: 
            self.connection.connect()
            sql = '''
                select * from book order by title
            '''
            return self.connection.query(sql).fetchall()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    def get(self, bookIsbn):
        try: 
            if not bookIsbn: return 'ISBN não informado'
            
            self.connection.connect()
            sql = '''
                select * from book where isbn = %s
            '''
            result = self.connection.query(sql, (bookIsbn,))
            return result.fetchone()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    def create(self, objData):
        try: 
            author = self.author.get(objData['author_id'])
            category = self.category.get(objData['category_id'])
            book = self.get(objData['isbn'])

            if not author: return 'Autor não encontrado'
            if not category: return 'Categoria não encontrado'
            if book: return 'Livro já cadastrado'

            self.connection.connect()
 
            sql = '''
                insert into book 
                (id, title, excerpt, description, price, author_id, category_id, isbn) 
                values (null, %s, %s, %s, %s, %s, %s, %s);
            '''
            data = ( 
                objData['title'],
                objData['excerpt'], 
                objData['description'], 
                objData['price'], 
                author['id'], 
                category['id'],
                objData['isbn'], 
            )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.listAll()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    def update(self, bookIsbn, objData):
        try: 
            if not bookIsbn: return 'ISBN não informado'

            book = self.get(bookIsbn)
            author = self.author.get(objData['author_id'])
            category = self.category.get(objData['category_id'])

            if not book: return 'Livro não encontrado'
            if not author: return 'Autor não encontrado'
            if not category: return 'Categoria não encontrado'
 
            self.connection.connect()

            sql = '''
                update book set title = %s, excerpt = %s, description = %s, 
                price = %s, author_id = %s, category_id = %s where isbn = %s;
            '''
            data = ( 
                objData['title'],
                objData['excerpt'], 
                objData['description'], 
                objData['price'], 
                objData['author_id'], 
                objData['category_id'],
                book['isbn'], 
            )
            self.connection.query(sql, data)
            self.connection.commit()
            return self.listAll()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    def delete(self, bookId):
        try: 
            self.connection.connect()
            sql = ''' delete from book where id = %s '''
            self.connection.query(sql, (bookId,))
            self.connection.commit()
        except Error as error: raise Exception(error)
        finally: self.connection.close()

    def details(self):
        try: 
            self.connection.connect()
            sql = ''' 
                select 
                    b.title livro, c.title categoria, b.isbn,
                    concat(a.first_name, ' ', a.second_name) as autor 
                from book b 
                inner join category c on b.category_id = c.id
                inner join author a on b.author_id = a.id;
            '''
            result = self.connection.query(sql)
            return result.fetchall()
        except Error as error: raise Exception(error)
        finally: self.connection.close()