from http import HTTPStatus
import jwt
from flask import request
from functools import wraps
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return {'message': 'Token is missing!'}, HTTPStatus.UNAUTHORIZED

        try:
            payload = jwt.decode(token, os.getenv("SECRET"), algorithms=["HS256"])
            # current_user = payload['sub']
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired!'}, HTTPStatus.UNAUTHORIZED
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token!'}, HTTPStatus.UNAUTHORIZED

        return f(*args, **kwargs)
    
    return decorated