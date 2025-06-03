from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/updusr', methods=['GET'])
def insertar_o_modificar_usuario():
    try:
        # Obtener parámetros 'id', 'nombre' y opcionalmente 'edad'
        user_id = request.args.get('id')
        nombre = request.args.get('nombre')
        edad = request.args.get('edad')  # Opcional

        # Validar los parámetros recibidos
        if not user_id or not nombre:
            return jsonify({
                "error": "Faltan parámetros obligatorios: 'id' y/o 'nombre'"
            }), 400

        if not user_id.isdigit():
            return jsonify({
                "error": "El parámetro 'id' debe ser un número"
            }), 400

        if edad and not edad.isdigit():
            return jsonify({
                "error": "El parámetro 'edad' debe ser un número"
            }), 400

        # Convertir los parámetros al formato adecuado
        user_id = int(user_id)
        edad = int(edad) if edad else None

        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            database='test'
        )

        cursor = conexion.cursor()

        # Comprobar si ya existe el registro con el ID proporcionado
        cursor.execute("SELECT id FROM usuarios WHERE id = %s", (user_id,))
        registro_existente = cursor.fetchone()

        if registro_existente:
            # Si el registro existe, realizar un UPDATE
            if edad is not None:
                consulta = "UPDATE usuarios SET nombre = %s, edad = %s WHERE id = %s"
                valores = (nombre, edad, user_id)
            else:
                consulta = "UPDATE usuarios SET nombre = %s WHERE id = %s"
                valores = (nombre, user_id)

            cursor.execute(consulta, valores)
            conexion.commit()

            mensaje = "Usuario actualizado correctamente"
        else:
            # Si no existe, realizar un INSERT
            if edad is not None:
                consulta = "INSERT INTO usuarios (id, nombre, edad) VALUES (%s, %s, %s)"
                valores = (user_id, nombre, edad)
            else:
                consulta = "INSERT INTO usuarios (id, nombre) VALUES (%s, %s)"
                valores = (user_id, nombre)

            cursor.execute(consulta, valores)
            conexion.commit()

            mensaje = "Usuario insertado correctamente"

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Responder con un mensaje de éxito
        return jsonify({
            "message": mensaje,
            "id": user_id,
            "nombre": nombre,
            "edad": edad
        }), 201

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
