from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/delusr', methods=['GET'])
def eliminar_usuario():
    try:
        # Obtener el parámetro 'id' de la solicitud
        user_id = request.args.get('id')

        # Validar que el parámetro 'id' exista y sea válido
        if not user_id:
            return jsonify({
                "error": "El parámetro 'id' es obligatorio"
            }), 400

        if not user_id.isdigit():
            return jsonify({
                "error": "El parámetro 'id' debe ser un número"
            }), 400

        # Convertir el 'id' a entero
        user_id = int(user_id)

        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            database='test'
        )

        cursor = conexion.cursor()

        # Comprobar si el registro existe
        cursor.execute("SELECT id FROM usuarios WHERE id = %s", (user_id,))
        registro_existente = cursor.fetchone()

        if not registro_existente:
            # Si el registro no existe, devolver error
            cursor.close()
            conexion.close()
            return jsonify({
                "error": f"No se encontró ningún usuario con id {user_id}"
            }), 404

        # Eliminar el registro
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        conexion.commit()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Responder con un mensaje de éxito
        return jsonify({
            "message": f"Usuario con id {user_id} eliminado correctamente"
        }), 200

    except mysql.connector.Error as e:
        # Manejar errores de conexión o SQL
        return jsonify({
            "error": "Error al conectar con la base de datos o realizar la operación",
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
