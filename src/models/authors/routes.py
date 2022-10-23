from flask import Blueprint, request
from src.models.authors.services import Author

author = Blueprint('author', __name__)
service = Author()

## Author routes
@author.route('/authors', methods=['GET'])
def getAuthors():
    response = service.listAll()
    return { 'authors': response }

@author.route('/author/<authorId>', methods=['GET'])
def getAuthor(authorId):
    response = service.get(authorId)
    return { 'author': response }

@author.route('/author', methods=['POST'])
def newAuthor():
    body = request.json
    response = service.create(body)
    return { 'authhor': response }

@author.route('/author/<authorId>', methods=['DELETE'])
def removeAuthor(authorId):
    service.delete(authorId)
    return { 'authhor': f'{authorId} deletado' }

@author.route('/author/<authorId>', methods=['PUT'])
def updateAuthor(authorId):
    body = request.json
    response = service.update(authorId, body)
    return { 'authhor': response }