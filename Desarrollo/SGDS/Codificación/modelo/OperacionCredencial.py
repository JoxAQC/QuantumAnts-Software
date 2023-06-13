import sqlite3 as sql
import os
import random
from Credencial import Credencial

class OperacionCredencial:
    def __init__(self) -> None:
        pass
    
    def generar_id_credencial(self):
        # Genera un número entero aleatorio de 7 dígitos
        id_credencial = random.randint(1000000, 9999999)
        return id_credencial
    
    def registrar_credencial(self, credencial):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instruction, (
            credencial.get_idCredencial(),
            credencial.get_fechaDeCreacion(),
            credencial.get_fechaDeExpiracion(),
            credencial.get_estado(),
            credencial.get_tipoDeUsuario(),
            credencial.get_username(),
            credencial.get_password()
        ))
        conn.commit()
        conn.close()

    def modificar_credencial(self, id_credencial, nuevo_estado):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "UPDATE Credencial SET estado = ? WHERE idCredencial = ?"
        cursor.execute(instruction, (nuevo_estado, id_credencial))
        conn.commit()
        conn.close()

    def buscar_credencial(self, id_credencial):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "SELECT * FROM Credencial WHERE idCredencial = ?"
        cursor.execute(instruction, (id_credencial,))
        result = cursor.fetchone()
        conn.close()
        return result

    def eliminar_credencial(self, id_credencial):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "DELETE FROM Credencial WHERE idCredencial = ?"
        cursor.execute(instruction, (id_credencial,))
        conn.commit()
        conn.close()

    def mostrar_todas_credenciales(self):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "SELECT * FROM Credencial"
        cursor.execute(instruction)
        result = cursor.fetchall()
        conn.close()
        return result
    

credencial1 = Credencial(505111, "12-12-12", "12-12-17", "Activo", "Donante","el miau", "lamala")

# Agregar Credenciales
oper_credencial = OperacionCredencial()
oper_credencial.registrar_credencial(credencial1)