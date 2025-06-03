for i in range(2, 21, 2):
    print(i)
#El asterisco * es un operador de desempaquetado. Se utiliza delante de un iterable,
# lo que hace es desempaquetar todos los elementos del iterable y pasarlos como argumentos individuales a la función.
print(*range(2, 21, 2), sep="\n")