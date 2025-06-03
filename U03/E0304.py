calificacion = int(input("Introduce tu calificación numérica (0-100): "))

if 90 <= calificacion <= 100:
    print("A")
elif 80 <= calificacion < 90:
    print("B")
elif 70 <= calificacion < 80:
    print("C")
elif 60 <= calificacion < 70:
    print("D")
else:
    print("F")
