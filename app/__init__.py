from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

#    # Import models AFTER db is initialized
#     from .models import User

     # Register blueprints AFTER models
    from .auth import auth_bp

    app.register_blueprint(auth_bp)  # register routes

    from .blog import blog_bp
    app.register_blueprint(blog_bp)


   
    @app.route("/")
    def home():
        return {"message": "Blog API is working!"}

    return app