class Contador:
    total = 0
    def __init__(self):
        Contador.total += 1
        
a = Contador()
b = Contador()
print(Contador.total)  # 2
