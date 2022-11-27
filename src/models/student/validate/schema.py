from jsonschema import validate, exceptions

studentSchema = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string"},
        "second_name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["first_name", "second_name", "email"]
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