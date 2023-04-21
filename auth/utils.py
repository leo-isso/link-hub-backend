import bcrypt


def generate_salt_key():
    return bcrypt.gensalt()


def encrypt_password(password, salt):
    return bcrypt.hashpw(password.encode(), salt).decode()


def validate_password(password, salt, user_password):
    encrypted_password = encrypt_password(password, salt)
    return encrypted_password == user_password
