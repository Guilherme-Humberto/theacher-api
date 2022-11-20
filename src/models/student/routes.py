from flask import Blueprint, request
from src.models.student.services.get import GetStudent
from src.models.student.services.create import CreateStudent

student = Blueprint('student', __name__)

@student.route('/student', methods=['GET'])
def getStudentById():
    response = GetStudent.execute()
    return { 'student': response }

@student.route('/student', methods=['POST'])
def createStudent():
    response = CreateStudent.execute()
    return { 'student': response }