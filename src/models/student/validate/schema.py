from jsonschema import validate, exceptions

createSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["name", "username", "email"]
}

findSchema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "password"]
}

def validateCreateSchema(jsonData):
    try:
        validate(
            instance=jsonData, 
            schema=createSchema
        )
    except exceptions.ValidationError as error:
        raise Exception(error)
    return True

def validateFindSchema(jsonData):
    try:
        validate(
            instance=jsonData, 
            schema=findSchema
        )
    except exceptions.ValidationError as error:
        raise Exception(error)
    return True