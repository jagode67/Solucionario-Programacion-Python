import random
import string

caracteres = string.ascii_letters + string.digits
longitud = 8
pwd=""
for i in range(longitud):
    pwd=pwd+random.choice(caracteres)
print(f"Contraseña generada: {pwd}")
