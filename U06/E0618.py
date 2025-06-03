import random

def adivina_numero():
    objetivo = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (1-100): "))
        intentos += 1
        if intento < objetivo:
            print("Más alto")
        elif intento > objetivo:
            print("Más bajo")
        else:
            print(f"¡Correcto! Intentos: {intentos}")
            break

adivina_numero()  
