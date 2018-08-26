import sys
import uuid

from flask import jsonify

from fcmbackend.logger import logger

from fcmbackend.api.exceptions import BadRequestException


def configure(app):
    """Configure the different error handlers"""

    def __create_message(code, default_message, error):
        message = error.message if getattr(error, 'message', None) is not None else default_message
        return jsonify({"code": code,
                        "error": message}), code

    @app.errorhandler(Exception)
    def handle_invalid_usage(error):
        correlation_id = uuid.uuid4().hex
        logger.error({"exception_type": sys.exc_info()[0],
                      "traceback": sys.exc_info()[2],
                      "correlation_id": correlation_id})
        return jsonify({"error": "Server error. Please, provide the correlation id number '{0}' to the server "
                                 "administrator".format(correlation_id)}), 500

    @app.errorhandler(BadRequestException)
    def bad_request(error):
        return __create_message(400, "Bad Request", error)
