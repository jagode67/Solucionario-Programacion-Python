from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/addProv')
def addProv():
    # Obtener parámetros de la solicitud GET
    cod = request.args.get('cod')
    provincia = request.args.get('provincia')

    # Validar que los parámetros no estén vacíos
    if not cod or not provincia:
        return jsonify({
            "error": "Faltan parámetros 'cod' y/o 'provincia'"
        }), 400

    try:
        # Validar que el código sea numérico
        if not cod.isdigit():
            return jsonify({
                "error": "El parámetro 'cod' debe ser numérico"
            }), 400

        # Abrir el archivo en modo append para agregar al final
        with open('prov.txt', 'a', encoding='utf-8') as file:
            file.write(f"{cod},{provincia}\n")

        # Devolver respuesta de éxito
        return jsonify({
            "message": "Provincia insertada correctamente",
            "codigo": cod,
            "provincia": provincia
        }), 200

    except Exception as e:
        # Manejo de errores
        return jsonify({
            "error": "Ocurrió un error al procesar la solicitud",
            "details": str(e)
        }), 500