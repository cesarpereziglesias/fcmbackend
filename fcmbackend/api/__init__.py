from functools import wraps

from flask import request
from cerberus import Validator

from fcmbackend.api.exceptions import BadRequestException


def parse_body(schema):

    def parse_body_decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            s = Validator(schema)
            if not s.validate(request.get_json()):
                raise BadRequestException(s.errors)

            return fn(*args, body_params=s.document, **kwargs)

        return wrapper

    return parse_body_decorator
