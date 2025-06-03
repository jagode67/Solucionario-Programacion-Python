
num_productos = int(input("¿Cuántos productos vas a ingresar? "))

precios = []
precios_con_descuento = []
for i in range(num_productos):

    precio = float(input(f"Introduce el precio del producto {i+1}: "))
    precios.append(precio)
    descuento = float(input("Introduce el porcentaje de descuento (0-100): "))

    precios_con_descuento.append((precio, precio * (1 - descuento / 100)))

print("\nPrecios con descuento:")
for precio_original, precio_descuento in precios_con_descuento:
    print(f"Precio original: {precio_original:.2f}, Precio con descuento: {precio_descuento:.2f}")


