total = 0
cont = 0

while True:
    num = float(input("Introducir un número (0 para finalizar): "))
    if num == 0:
        break
    total += num
    cont += 1

if cont > 0:
    average = total / cont
    print(f"La media de los {cont} numeros es: {average}")
else:
    print("Ningún número introducido")