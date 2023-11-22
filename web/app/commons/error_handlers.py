from flask import jsonify


def exception_handler(err: Exception):
    response = jsonify({'error': str(err)})
    response.status_code = 423
    return response
