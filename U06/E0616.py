def agregar_contacto(contactos, **kwargs):
    contactos.append(kwargs)
    return contactos

contactos = []
agregar_contacto(contactos, nombre="Ana", telefono="123456")
agregar_contacto(contactos, nombre="Lara", telefono="654321")
print(contactos)  
