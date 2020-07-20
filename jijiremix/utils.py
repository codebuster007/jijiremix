import string
import secrets

def generate_random_token(n):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(n))
