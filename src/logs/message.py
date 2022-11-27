from json import dumps

def logError(message, status):
    return dumps({ "error": message }), status

def logSuccess(message, status):
    return dumps({ "success": message }), status