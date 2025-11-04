from flask import abort, redirect, session
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def apology(message=None, code=400):
    """Fallback error handler using Flask default."""
    if message:
        return f"{code} Error: {message}", code
    else:
        abort(code)
