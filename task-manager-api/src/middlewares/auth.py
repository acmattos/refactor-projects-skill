import hmac
import hashlib
import functools
from flask import request, jsonify
from config import settings


def generate_token(user_id):
    sig = hmac.new(
        settings.SECRET_KEY.encode(),
        str(user_id).encode(),
        hashlib.sha256
    ).hexdigest()
    return f"{user_id}:{sig}"


def verify_token(token):
    try:
        user_id_str, sig = token.split(':', 1)
        user_id = int(user_id_str)
        expected = hmac.new(
            settings.SECRET_KEY.encode(),
            str(user_id).encode(),
            hashlib.sha256
        ).hexdigest()
        if hmac.compare_digest(sig, expected):
            return user_id
    except Exception:
        pass
    return None


def require_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            token = request.headers.get('X-Token', '')
        if not verify_token(token):
            return jsonify({'error': 'Autenticação necessária'}), 401
        return f(*args, **kwargs)
    return decorated
