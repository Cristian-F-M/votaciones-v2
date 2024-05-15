from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("Config.Config")

    db.init_app(app)
    bcrypt.init_app(app)    

    from app.routes import main, user
    app.register_blueprint(main.bp)
    app.register_blueprint(user.bp)

    return app