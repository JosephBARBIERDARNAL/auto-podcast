import random
import string

def generate_random_id(length=10):
    """Generate a random string of alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))