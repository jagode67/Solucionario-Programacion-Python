import xml.etree.ElementTree as ET

def gestionar_biblioteca_xml():
    try:
        # Crear estructura XML
        biblioteca = ET.Element("biblioteca")
        
        # Añadir libros
        libros = [
            {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "año": 1605},
            {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
            {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año": 1943}
        ]
        
        for libro_info in libros:
            libro = ET.SubElement(biblioteca, "libro")
            ET.SubElement(libro, "titulo").text = libro_info["titulo"]
            ET.SubElement(libro, "autor").text = libro_info["autor"]
            ET.SubElement(libro, "año").text = str(libro_info["año"])
        
        # Guardar XML
        tree = ET.ElementTree(biblioteca)
        tree.write("biblioteca.xml", encoding="utf-8", xml_declaration=True)
        print("Archivo XML creado correctamente.")
        
        # Leer XML y mostrar información
        tree = ET.parse("biblioteca.xml")
        root = tree.getroot()
        
        print("\nLibros en la biblioteca:")
        for i, libro in enumerate(root.findall("libro"), 1):
            titulo = libro.find("titulo").text
            autor = libro.find("autor").text
            año = libro.find("año").text
            print(f"{i}. '{titulo}' de {autor} ({año})")
            
    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la función
gestionar_biblioteca_xml()