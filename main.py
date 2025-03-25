import flask
import re

# TODO: change this to your academic email
AUTHOR = "hajoon@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations

def validate_password(pw):
    if len(pw) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in pw):
        return False, "Password must contain at least one uppercase letter."
    if not any(c.isdigit() for c in pw):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*]", pw):
        return False, "Password must contain at least one special character (!@#$%^&*)."
    
    return True, "Password is valid."


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    is_valid, reason = validate_password(pw)

    # FIXME: to be implemented
    return flask.jsonify({"valid": is_valid, "reason": reason}), (200 if is_valid else 400)



