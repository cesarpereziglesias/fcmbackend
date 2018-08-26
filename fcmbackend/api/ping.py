from flask import Blueprint

mod = Blueprint('ping', __name__)


@mod.route('/')
def ping():
    return 'PONG'
