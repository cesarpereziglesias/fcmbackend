import logging


def configure_application_logger():
    """

    :return:
    """
    logger_werkzeug = logging.getLogger('werkzeug')
    logger_werkzeug.setLevel(logging.ERROR)

    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger_fcmbackend = logging.getLogger('fcmbackend')
    logger_fcmbackend.setLevel(logging.DEBUG)
    logger_fcmbackend.addHandler(fh)
    logger_fcmbackend.addHandler(ch)

    return logger_fcmbackend


logger = configure_application_logger()
