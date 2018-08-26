from fcmbackend.repository import fcm as fcm_repository


def register(identifier, token):
    fcm_repository.register(identifier, token)
