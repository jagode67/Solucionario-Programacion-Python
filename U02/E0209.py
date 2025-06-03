producto1 = "Manzanas"
precio1 = 2.5
producto2 = "Peras"
precio2 = 9.75

print(f"""FACTURA
{producto1:.<15}{precio1:>7.2f}€
{producto2:.<15}{precio2:>7.2f}€
{'Total':.<15}{precio1 + precio2:>7.2f}€""")