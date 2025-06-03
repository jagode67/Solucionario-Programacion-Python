import random

numero_secreto = random.randint(1, 100)
intento = 0
adivinado = False
veces=1

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento == numero_secreto:
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número a la {veces} vez.")
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
    veces+=1
