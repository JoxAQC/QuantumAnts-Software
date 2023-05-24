import os
import sqlite3 as sql

class Credencial:
    def __init__(self, idCredencial,fechaDeCreacion,fechaDeExpiracion,estado,tipoDeUsuario,username,password):
        self.__idCredencial = idCredencial
        self.__fechaDeCreacion =fechaDeCreacion
        self.__fechaDeExpiracion =fechaDeExpiracion
        self.__estado =estado
        self.__tipoDeUsuario =tipoDeUsuario
        self.__username =username
        self.__password = password

def insertar_credencial(idCredencial, fechaDeCreacion, fechaDeExpiracion, estado, tipoDeUsuario, username, password):
    # Obtener la ruta absoluta del directorio actual
    current_dir = os.path.abspath("")
    # Construir la ruta absoluta del archivo de la base de datos
    db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
    # Establecer la conexión a la base de datos
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruction = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(instruction, (idCredencial, fechaDeCreacion, fechaDeExpiracion, estado, tipoDeUsuario, username, password))
    conn.commit()
    conn.close()


    
        