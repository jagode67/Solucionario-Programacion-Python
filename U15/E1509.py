from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/insusr', methods=['GET'])
def inusr():
    try:
        # Obtener parámetros 'id', 'nombre' y opcionalmente 'edad'
#        user_id = request.args.get('id')
        nombre = request.args.get('nombre')
        edad = request.args.get('edad')  # Opcional

        # Validar los parámetros recibidos
#        if not user_id or not nombre:
#            return jsonify({
#                "error": "Faltan parámetros obligatorios: 'id' y/o 'nombre'"
#            }), 400

#        if not user_id.isdigit():
#            return jsonify({
#                "error": "El parámetro 'id' debe ser un número"
#            }), 400

        if edad and not edad.isdigit():
            return jsonify({
                "error": "El parámetro 'edad' debe ser un número"
            }), 400

        # Convertir los parámetros al formato adecuado
#        user_id = int(user_id)
        edad = int(edad) if edad else None

        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            database='test'
        )

        cursor = conexion.cursor()

        # Preparar la consulta de inserción
        if edad is not None:
            consulta = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
            valores = (nombre, edad)
        else:
            consulta = "INSERT INTO usuarios (nombre) VALUES (%s)"
            valores = (nombre,)

        # Ejecutar la consulta
        cursor.execute(consulta, valores)
        conexion.commit()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Responder con un mensaje de éxito
        return jsonify({
            "message": "Usuario insertado correctamente",
            "nombre": nombre,
            "edad": edad
        }), 201

    except mysql.connector.Error as e:
        # Manejar errores de conexión o SQL
        return jsonify({
            "error": "Error al conectar con la base de datos o realizar la inserción",
            "details": str(e)
        }), 500

    except Exception as e:
        # Manejar errores generales
        return jsonify({
            "error": "Ocurrió un error inesperado",
            "details": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
