from flask import Blueprint, request
from src.models.course.services.get import GetCourse
from src.models.course.services.list import ListCourse
from src.models.course.services.create import CreateCourse

course = Blueprint('course', __name__)

@course.route('/course', methods=['GET'])
def getCourseById():
    response = GetCourse.execute()
    return { 'course': response }

@course.route('/courses', methods=['GET'])
def getAllCourses():
    response = ListCourse.execute()
    return { 'course': response }

@course.route('/course', methods=['POST'])
def createCourse():
    response = CreateCourse.execute()
    return { 'course': response }