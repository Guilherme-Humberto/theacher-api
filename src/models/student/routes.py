from flask import Blueprint, request
from src.models.student.validate.schema import validateStudentSchema
from src.models.student.services import get
from src.models.student.services import create

student = Blueprint('student', __name__)

@student.route('/student', methods=['GET'])
def getStudentById():
    getStudent = get.GetStudent()
    response = getStudent.execute()
    
    return { 'student': response }

@student.route('/student', methods=['POST'])
def createStudent():
    body = request.json
    validateStudentSchema(body)

    createStudent = create.CreateStudent(body)

    response = createStudent.execute()
    return response