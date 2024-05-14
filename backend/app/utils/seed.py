from app.models.Type_document import Type_document
from app.models.Role import Role
from app import db
import uuid

types_document = {
    "model": Type_document,
    "data": [
        Type_document(id=uuid.uuid4(), name="Cédula de ciudadanía"),
        Type_document(id=uuid.uuid4(), name="Tarjeta de identidad"),
        Type_document(id=uuid.uuid4(), name="Cédula de extranjería"),
        Type_document(id=uuid.uuid4(), name="Pasaporte"),
    ],
}

roles = {
    "model": Role,
    "data": [
        Role(id=uuid.uuid4(), name="User"),
        Role(id=uuid.uuid4(), name="Admin"),
        Role(id=uuid.uuid4(), name="Candidate"),
    ],
}


seeds = [types_document, roles]


def seed_database():
    for seed in seeds:
        if seed["model"].query.count() > 0:
            continue
        for data in seed["data"]:
            db.session.add(data)
    db.session.commit()
