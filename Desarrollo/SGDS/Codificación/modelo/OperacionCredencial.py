import sqlite3 as sql
import os
import random


class OperacionCredencial:
    def __init__(self) -> None:
        pass
    
    def generar_id_credencial(self):
        # Genera un número entero aleatorio de 7 dígitos
        id_credencial = random.randint(1000000, 9999999)
        return id_credencial
    
    def registrar_credencial(credencial):
        conn = sql.connect("modelo/SGDS-VABD01.db")
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
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        instruction = "UPDATE Credencial SET estado = ? WHERE idCredencial = ?"
        cursor.execute(instruction, (nuevo_estado, id_credencial))
        conn.commit()
        conn.close()

    def buscar_credencial(self, id_credencial):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        instruction = "SELECT * FROM Credencial WHERE idCredencial = ?"
        cursor.execute(instruction, (id_credencial,))
        result = cursor.fetchone()
        conn.close()
        return result

    def eliminar_credencial(id):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        instruction = "DELETE FROM Credencial where idCredencial= ?"
        cursor.execute(instruction, (id))
        conn.commit()
        conn.close()

    def mostrar_todas_credenciales(self):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        instruction = "SELECT * FROM Credencial"
        cursor.execute(instruction)
        result = cursor.fetchall()
        conn.close()
        return result
