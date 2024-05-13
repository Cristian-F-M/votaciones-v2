from app import create_app, db
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()