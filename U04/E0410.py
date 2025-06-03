# Inicializar variables
total_expenses = 0
total_income = 0

# Obtiene gastos
print("Introducir gastos (0 para finalizar):")
while True:
    expense = float(input("Gasto: "))
    if expense == 0:
        break
    total_expenses += expense

# Obtener ingresos
print("\nIntroducir ingresos (0 para finalizar):")
while True:
    income = float(input("Ingreso: "))
    if income == 0:
        break
    total_income += income

# Calcula balance
balance = total_income - total_expenses

# Muestra resultado
print("\nResumem mensual:")
print(f"Total gastos: {total_expenses:.2f}")
print(f"Total ingresos: {total_income:.2f}")
if balance > 0:
    print(f"Has ganado: {balance:.2f}")
elif balance < 0:
    print(f"Has perdido: {abs(balance):.2f}")
else:
    print("Saldo 0")