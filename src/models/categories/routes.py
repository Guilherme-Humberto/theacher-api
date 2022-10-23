from flask import Blueprint, request
from src.models.categories.services import Category

category = Blueprint('category', __name__)
service = Category()

## Category routes
@category.route('/categories', methods=['GET'])
def getCategories():
    response = service.listAll()
    return { 'categories': response }

@category.route('/category/<categoryId>', methods=['GET'])
def getCategory(categoryId):
    response = service.get(categoryId)
    return { 'category': response }

@category.route('/category', methods=['POST'])
def newCategory():
    body = request.json
    response = service.create(body)
    return { 'category': response }

@category.route('/category/<categoryId>', methods=['DELETE'])
def removeCategory(categoryId):
    service.delete(categoryId)
    return { 'category': f'{categoryId} deletado' }

@category.route('/category/<categoryId>', methods=['PUT'])
def updateCategory(categoryId):
    body = request.json
    response = service.update(categoryId, body)
    return { 'category': response }
