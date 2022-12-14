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
