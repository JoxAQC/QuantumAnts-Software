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
        conn = sql.connect(db_path)
        return conn

def entregaBeneficios(idCredencial):
    conn = conectar_bd()
    cursor = conn.cursor()

    beneficio_random = random.choice(Beneficios)

    try:
        cursor.execute("SELECT desripcion FROM Beneficio WHERE idHospital = ?",(idCredencial,))
        valor_actual = cursor.fetchone()[0]
        nuevo_valor = valor_actual + f"\n{beneficio_random}"

        cursor.execute("UPDATE Beneficio SET desripcion = ? WHERE idHospital = ?",(nuevo_valor,idCredencial))
        conn.commit()
        print("Beneficio registrado correctamente.")
    except sql.Error as e:
         print("Error al entregar beneficios:",str(e))



    cursor.close
    conn.close