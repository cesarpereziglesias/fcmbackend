from fcmbackend.exceptions import FCMBackendException


class ApiException(FCMBackendException):
    """Class representing exception raised in API environment"""


class BadRequestException(ApiException):
    """Class representing exception raised when the request has done with wrong parameters"""
