from flask import Blueprint, jsonify

from fcmbackend.api import parse_body
from fcmbackend.controller import fcm as fcm_controller

from fcmbackend.api.validators.fcm import SCHEMA_BODY_REGISTER
mod = Blueprint('fcm', __name__)


@mod.route('/', methods=['POST'])
@parse_body(SCHEMA_BODY_REGISTER)
def register(body_params):
    fcm_controller.register(body_params.get('identifier'), body_params.get('token'))
    return jsonify('register()'), 201


@mod.route('/<identifier>/send_message', methods=['POST'])
def send_message(identifier):
    return jsonify("send_message({})".format(identifier)), 204
