from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/delProv', methods=['GET'])
def delProv():
    # Obtener parámetro 'cod' de la solicitud GET
    cod = request.args.get('cod')

    # Validar que el parámetro no esté vacío
    if not cod:
        return jsonify({
            "error": "Falta el parámetro 'cod'"
        }), 400

    try:
        # Validar que el código sea numérico
        if not cod.isdigit():
            return jsonify({
                "error": "El parámetro 'cod' debe ser numérico"
            }), 400

        # Leer el archivo y filtrar las líneas que no correspondan al código
        with open('prov.txt', 'r', encoding='utf-8') as file:
            provincias = file.readlines()

        # Filtrar las provincias que no coinciden con el código
        provincias_filtradas = [linea for linea in provincias if not linea.startswith(cod + ',')]

        # Si no se encontró ninguna provincia para eliminar, retornar un error
        if len(provincias_filtradas) == len(provincias):
            return jsonify({
                "error": "Código de provincia no encontrado"
            }), 404

        # Escribir el archivo nuevamente con las provincias restantes
        with open('prov.txt', 'w', encoding='utf-8') as file:
            file.writelines(provincias_filtradas)

        # Devolver respuesta de éxito
        return jsonify({
            "message": "Provincia eliminada correctamente",
            "codigo": cod
        }), 200

    except Exception as e:
        # Manejo de errores
        return jsonify({
            "error": "Ocurrió un error al procesar la solicitud",
            "details": str(e)
        }), 500

