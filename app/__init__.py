from flask import Flask
from app.Views.author import author_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(author_bp)
    return app
