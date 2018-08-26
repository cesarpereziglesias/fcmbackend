class FCMBackendException(Exception):
    """Class representing exception raised in FCMBackend"""

    def __init__(self, message=None):
        """
        Creates FCMBackendException

        :param message:
        """
        self.message = message
