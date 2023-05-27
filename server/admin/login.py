import jwt
import time

from main import conf

SECRET_KEY = conf['secret']
ALGORITHM = conf['algorithm']
JWT_EXPIRES_MINUTES = conf['jwt_expires_minutes']
REFRESH_EXPIRES_DAYS = conf['refresh_expires_days']

def check_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload['expires'] <= time.time():
            payload=None
    except Exception as e:
        payload = None
    return payload!=None

def create_jwt_token(login, password):
    payload = {
        'login': login,
        'password': password,
        'expires': time.time()+60*JWT_EXPIRES_MINUTES
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(login, password):
    pass