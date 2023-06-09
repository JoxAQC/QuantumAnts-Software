import sqlite3 as sql
import os

def conectar_bd():  
    # Obtener la ruta absoluta al archivo de base de datos
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

    # Establecer conexión con la base de datos
    conn = sql.connect(db_path)
    return conn

def buscar_usuario(user, password):
    conn = sql.connect("serializar/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM Credencial WHERE user = ? AND password = ?",
            (user, password),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None