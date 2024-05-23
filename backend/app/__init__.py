from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from env import ACEPTED_ORIGIN

print(ACEPTED_ORIGIN)

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("Config.Config")

    db.init_app(app)
    bcrypt.init_app(app)    
    Migrate(app, db)

    CORS(app, supports_credentials=True, resources={
        r"/*": {
            "origins": [ACEPTED_ORIGIN]
        }
    })

    from app.routes import main, user, resources
    app.register_blueprint(main.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(resources.bp)

    return app