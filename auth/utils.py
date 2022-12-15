import hashlib
import string

import secrets


def generate_salt_key():
    return "".join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase)
        for _ in range(20)
    )


def encrypt_password(password, salt):
    salted_password = f"{password}{salt}"
    return hashlib.md5(salted_password.encode()).hexdigest()


def validate_password(password, salt, user_password):
    encrypted_password = encrypt_password(password, salt)
    return encrypted_password == user_password
