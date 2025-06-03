def validar_password(contra):
    if len(contra) < 8:
        return False
    if not any(c.isupper() for c in contra):
        return False
    if not any(c.isdigit() for c in contra):
        return False
    return True

print(validar_password("Pass1234"))  # True

