class EdadInvalidaError(Exception):
    def __init__(self, mensaje, codigo):
        self.message = mensaje
        self.codigo = codigo

def validar_edad(edad):
    try:
        edad = int(edad)
        if edad < 18:
            raise EdadInvalidaError("La edad debe ser mayor o igual a 18", 1001)
        elif edad > 100:
            raise EdadInvalidaError("La edad debe ser menor o igual a 100", 1002)
        print(f"La edad {edad} es válida.")
    except ValueError:
        print("Error: Debes introducir un número.")
    except EdadInvalidaErr as e:
        print(f"Error {e.codigo}: {e.message}")

# Pruebas
validar_edad(25)  # La edad 25 es válida
validar_edad(15)  # Error 1001: La edad debe ser mayor o igual a 18
validar_edad(120)  # Error 1002: La edad debe ser menor o igual a 100
validar_edad("abc")  # Error: Debes introducir un número