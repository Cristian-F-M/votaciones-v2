from app import create_app, db
from dotenv import load_dotenv
from app.utils.seed import seed_database

load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()
    seed_database()

if __name__ == "__main__":
    app.run()