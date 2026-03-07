import re

def validate_email(email):
    """Memvalidasi apakah input adalah format email yang benar."""
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.search(regex, email):
        return True
    return False