from flask import Flask
from src.models.authors.routes import author
from src.models.categories.routes import category
from src.models.books.routes import book

app = Flask(__name__)

app.register_blueprint(category)
app.register_blueprint(book)
app.register_blueprint(author)