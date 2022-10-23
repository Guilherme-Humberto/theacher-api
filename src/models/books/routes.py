from flask import Blueprint, request
from src.models.books.services import Book

book = Blueprint('book', __name__)
service = Book()

## Book routes
@book.route('/books', methods=['GET'])
def getBooks():
    response = service.listAll()
    return { 'books': response }

@book.route('/book/<bookIsbn>', methods=['GET'])
def getBook(bookIsbn):
    response = service.get(bookIsbn)
    return { 'book': response }

@book.route('/book/details', methods=['GET'])
def getBooksDetails():
    response = service.details()
    return { 'book': response }

@book.route('/book', methods=['POST'])
def newBook():
    body = request.json
    response = service.create(body)
    return { 'book': response }

@book.route('/book/<bookId>', methods=['DELETE'])
def removeBook(bookId):
    service.delete(bookId)
    return { 'book': 'livro deletado' }

@book.route('/book/<bookIsbn>', methods=['PUT'])
def updateBook(bookIsbn):
    body = request.json
    response = service.update(bookIsbn, body)
    return { 'book': response }