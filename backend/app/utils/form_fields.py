import re

user_fields_validations = {
    "name": {
        "func": lambda x: len(x) >= 3,
        "message": "Name must have at least 3 characters",
        "required": True,
    },
    "lastname": {
        "func": lambda x: len(x) >= 3,
        "message": "Lastname must have at least 3 characters",
        "required": True,
    },
    "email": {
        "func": lambda x: re.match(email_pattern, x),
        "message": "Invalid email format",
        "required": True,
    },
    "type_document": {
        "func": lambda x: isinstance(x, str),
        "message": "Type document is not valid",
        "required": True,
    },
    "document": {
        "func": lambda x: len(x) >= 8,
        "message": "Document must have at least 8 characters",
        "required": True,
    },
    "phone": {
        "func": lambda x: len(x) >= 10,
        "message": "Phone must have at least 10 characters",
        "required": False,
    },
    "password": {
        "func": lambda x: 8 <= len(x) <= 20,
        "message": "Password must have between 8 and 20 characters",
        "required": True,
    },
}


email_pattern = r"^[a-zA-Z0-9._%+-]{3,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
user_required_fields = [
    field
    for field, validation in user_fields_validations.items()
    if validation.get("required", False)
]


def response_integrity_error(error, sentence, fields):
    error = str(error)

    if sentence in error:
        for field in fields:
            if field in error:
                field  = field.split(".")[-1]
                return {"field": field, "message": f"{field.capitalize()} already exists"}
    return { "message": f"An error occurred, please try again later {error}"}