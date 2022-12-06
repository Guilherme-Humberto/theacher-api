from jsonschema import validate, exceptions

studentSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["name", "username", "email"]
}

def validateStudentSchema(jsonData):
    try:
        validate(
            instance=jsonData, 
            schema=studentSchema
        )
    except exceptions.ValidationError as error:
        raise Exception(error)
    return True