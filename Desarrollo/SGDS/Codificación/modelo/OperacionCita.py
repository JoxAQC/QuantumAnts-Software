import os
import sqlite3 as sql

class OperacionCita:
    def __init__(self):
        pass
    
    def confirmarCita(self, cita):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        instruction = "SELECT COUNT(*) FROM Credencial WHERE idCita = ?"
        cursor.execute(instruction, (cita.get_idCita(),))
        result = cursor.fetchone()[0]

        conn.close()

        if result > 0:
            return True
        else:
            return False
    
    def finalizarCita(self, cita):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        instruction = "DELETE FROM Credencial WHERE idCita = ?"
        cursor.execute(instruction, (cita.get_idCita(),))
        conn.commit()

        conn.close()
    
    def programarCita(self, donante, horario):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        id_donante = donante.get_id_donante()
        fecha = horario.get_fecha()
        estado = True  # Valor predeterminado para el campo estado

        # Insertar la nueva cita en la base de datos sin incluir el campo idCita
        instruction = "INSERT INTO Cita (fecha, idDonante, idHospital, estado) VALUES (?, ?, ?, ?)"
        cursor.execute(instruction, (fecha, id_donante, horario.get_idHospital(), estado))
        conn.commit()

        # Obtener el idCita generado automáticamente
        id_cita = cursor.lastrowid

        # Actualizar la fila de la cita para incluir el idCita
        update_instruction = "UPDATE Cita SET idCita = ? WHERE idCita = ?"
        cursor.execute(update_instruction, (id_cita, id_cita))
        conn.commit()

        conn.close()
        return True  # La cita se programó correctamente

    def reprogramarCita(self, cita, fecha_nueva):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        id_cita = cita.get_idCita()

        instruction = "UPDATE Credencial SET fecha = ? WHERE idCita = ?"
        cursor.execute(instruction, (fecha_nueva, id_cita))
        conn.commit()

        conn.close() 
        
    def verCitas(self, donante, sistema):
        conn = sistema.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM citas WHERE idDonante = ?", (donante.get_id_donante(),))
            citas = cursor.fetchall()

            if len(citas) > 0:
                print("Citas:")
                for cita in citas:
                    print(f"Fecha: {cita[1]}, Hospital: {cita[2]}, Estado: {cita[3]}")
            else:
                print("No se encontraron citas para este donante.")

        except sql.Error as error:
            print("Error al acceder a la base de datos:", error)

        finally:
            conn.close()


        