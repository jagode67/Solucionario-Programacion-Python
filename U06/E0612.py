import random
import string

def generar_password(longitud=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print(generar_password(10))  # Ejemplo: aB3$kL9!pQ
