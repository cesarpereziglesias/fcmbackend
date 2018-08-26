from flask import Flask
from flask.logging import default_handler

from fcmbackend import error_handler

from fcmbackend.logger import logger

import fcmbackend.api.ping
import fcmbackend.api.fcm


class LoggerMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        logger.info({"path": environ.get("PATH_INFO"),
                     "method": environ.get("REQUEST_METHOD"),
                     "remote_ip": environ.get("REMOTE_ADDR")})
        return self.app(environ, start_response)


def create_app():
    """
    Create the base Flask Application
    """
    flask_app = Flask(__name__)
    flask_app.logger.removeHandler(default_handler)

    # Assign modules
    flask_app.register_blueprint(fcmbackend.api.ping.mod, url_prefix='/ping')
    flask_app.register_blueprint(fcmbackend.api.fcm.mod, url_prefix='/fcm')

    error_handler.configure(flask_app)

    flask_app.wsgi_app = LoggerMiddleware(flask_app.wsgi_app)

    logger.info("Application has started")
    return flask_app


app = create_app()
