from flask import Flask
from src.models.course.routes import course
from src.models.student.routes import student
from src.models.teacher.routes import teacher

app = Flask(__name__)

app.register_blueprint(course)
app.register_blueprint(student)
app.register_blueprint(teacher)