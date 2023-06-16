import sqlite3 as sql
import os
import random

Beneficios = ["Consulta gratis Psicologia","Consulta gratis dentista","Consulta gratis Dermatologia","Consulta gratis oftalmologia"
              ,"Consulta gratis Medicina General"]

def conectar_bd():  
        # Obtener la ruta absoluta al archivo de base de datos
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

        # Establecer conexión con la base de datos
        conn = sql.connect("modelo/SGDS-VABD01.db")
        return conn

def entregar_beneficios(idDonante):
    conn = conectar_bd()
    cursor = conn.cursor()

    beneficio_random = random.choice(Beneficios)

    try:
        cursor.execute("SELECT beneficioActivo FROM Donante WHERE idDonante = ?",(idDonante,))
        valor_actual = cursor.fetchone()[0]
        nuevo_valor = valor_actual + f"\n{beneficio_random}"

        cursor.execute("UPDATE Donante SET beneficioActivo = ? WHERE idDonante = ?",(nuevo_valor,idDonante))
        conn.commit()
        print("Beneficio registrado correctamente.")
    except sql.Error as e:
         print("Error al entregar beneficios:",str(e))

    cursor.close()
    conn.close()

def validar_condiciones(idHospital):
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT cantidadSangre FROM Beneficio WHERE idHospital = ? ",(idHospital,))
        cantidad_sangre = cursor.fetchone()[0]
        if(cantidad_sangre > 0):
             return True
        else:
             return False
    except sql.Error as e:
        print("Error al validar condiciones de beneficio:",str(e))

    cursor.close()
    conn.close()