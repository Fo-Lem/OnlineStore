import jwt
import time

from admin.api import add_entity
from database.structure import refresh_tokens
from main import auth_conf

SECRET_KEY = auth_conf['secret']
ALGORITHM = auth_conf['algorithm']
JWT_EXPIRES_MINUTES = auth_conf['jwt_expires_minutes']
REFRESH_EXPIRES_DAYS = auth_conf['refresh_expires_days']

def check_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload['expires'] <= time.time():
            payload=None
    except Exception as e:
        payload = None
    return payload!=None

def create_jwt_token(login):
    payload = {
        'login': login,
        'expires': time.time()+60*JWT_EXPIRES_MINUTES
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(login):
    payload = {
        'login': login,
        'expires': time.time()+60*24*REFRESH_EXPIRES_DAYS
    }
    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    add_entity(refresh_tokens, id=refresh_token)
    return refresh_token

def get_payload(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        payload = None
    return payload