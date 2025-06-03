from flask import Flask, request, jsonify
import mysql.connector
import sqlite3

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def usuarios():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        database='test'
    )
    # conexion=sqlite3.connect("j.db") SQLite
    cursor = conexion.cursor()
    cursor.execute("SELECT id,nombre,edad FROM usuarios")
    regs = cursor.fetchall()
    # Crear una lista de diccionarios a partir de los resultados
    usuarios = [
        {"id": reg[0], "nombre": reg[1], "edad": reg[2]}
        for reg in regs
    ]
    cursor.close()
    conexion.close()
    return jsonify(usuarios),200

