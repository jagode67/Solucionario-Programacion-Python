class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
    def extraer(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad

c = CuentaBancaria(100)
c.depositar(50)
c.extraer(30)
c.extraer(200) # Fondos insuficientes
print(c.saldo) # 120
