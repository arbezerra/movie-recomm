import jwt
from app import config
import traceback


def verify(token):
    if not token:
        return False
    token = token.split()[1]
    try:
        data = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
        return data
    except Exception:
        print(traceback.format_exc())
        return False
