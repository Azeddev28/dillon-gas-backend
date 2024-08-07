import string
import secrets


def create_order_key():
    return ''.join(secrets.choice(string.digits) for i in range(6))
