from flask import Blueprint, request
from src.models.student.validate.schema import validateCreateSchema, validateFindSchema
from src.models.student.services import get
from src.models.student.services import create

student = Blueprint('student', __name__)

@student.route('/student', methods=['GET'])
def getStudent():
    body = request.json
    validateFindSchema(body)

    getStudent = get.GetStudent(body)
    response = getStudent.execute()
    
    return { 'student': response }

@student.route('/student', methods=['POST'])
def createStudent():
    body = request.json
    validateCreateSchema(body)

    createStudent = create.CreateStudent(body)

    response = createStudent.execute()
    return response