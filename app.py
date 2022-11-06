from flask import Flask
from src.models.example.routes import example

app = Flask(__name__)

app.register_blueprint(example)