from flask import Blueprint, request
from src.models.example.services import Example

example = Blueprint('example', __name__)
service = Example()

@example.route('/examples', methods=['GET'])
def getExamples():
    response = service.listAll()
    return { 'examples': response }