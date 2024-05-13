from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import uuid


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config.from_object("Config.Config")

    db.init_app(app)


    from app.routes import main
    app.register_blueprint(main.bp)

    return app