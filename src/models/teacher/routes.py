from flask import Blueprint, request
from src.models.teacher.services.get import GetTeacher
from src.models.teacher.services.list import ListTeacher
from src.models.teacher.services.create import CreateTeacher

teacher = Blueprint('teacher', __name__)

@teacher.route('/teacher', methods=['GET'])
def getTeacheryId():
    response = GetTeacher.execute()
    return { 'teacher': response }

@teacher.route('/teachers', methods=['GET'])
def getAllTeachers():
    response = ListTeacher.execute()
    return { 'teacher': response }

@teacher.route('/teacher', methods=['POST'])
def createTeacher():
    response = CreateTeacher.execute()
    return { 'teacher': response }