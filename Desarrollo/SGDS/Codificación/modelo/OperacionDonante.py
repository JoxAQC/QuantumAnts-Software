import sqlite3 as sql
import os

class OperacionDonante:
    def __init__(self):
        pass
    
    def registrar_donante(self, donante):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        try:
            instruction = "INSERT INTO Donante VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                instruction,
                (
                    donante.get_id_donante(),
                    donante.get_nombre(),
                    donante.get_fecha_nacimiento(),
                    donante.get_dni(),
                    donante.get_telefono(),
                    donante.get_direccion(),
                    donante.get_beneficio_activo(),
                    donante.get_grupo_sanguineo(),
                    donante.get_rh(),
                    donante.get_ultima_donacion(),
                    donante.get_id_hospitalUltimo(),
                ),
            )

            conn.commit()
            print("Donante registrado exitosamente.")
        except sql.Error as e:
            print("Error al registrar el donante:", str(e))

        conn.close()

    def buscar_donantes(self, donante, sistema):
        conn = sistema.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM Donante WHERE grupo_sanguineo = ? AND direccion LIKE ?",
                (donante.get_grupo_sanguineo(), f"%{donante.get_direccion()}%"),
            )

            donantes = cursor.fetchall()

            return donantes
        except sql.Error as e:
            print("Error al buscar donantes:", str(e))

        conn.close()
        return []

    def cambiar_datos(self, donante, sistema):
        conn = sistema.conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Donante SET nombre = ?, fecha_nacimiento = ?, dni = ?, telefono = ?, "
                "direccion = ? WHERE idDonante = ?",
                (
                    donante.get_nombre(),
                    donante.get_fecha_nacimiento(),
                    donante.get_dni(),
                    donante.get_telefono(),
                    donante.get_direccion(),
                    donante.get_id_donante()
                ),
            )

            conn.commit()
            print("Datos actualizados exitosamente.")
        except sql.Error as e:
            print("Error al actualizar los datos:", str(e))

        conn.close()

    def eliminar_donante(self, donante, sistema):
        conn = sistema.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM Donante WHERE idDonante = ?", (donante.get_id_donante(),))

            conn.commit()
            print("Donante eliminado exitosamente.")
        except sql.Error as e:
            print("Error al eliminar el donante:", str(e))

        conn.close()

    def ver_donantes(self, sistema):
        conn = sistema.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Donante")

            donantes = cursor.fetchall()

            if donantes:
                for donante in donantes:
                    print(f"ID: {donante[0]}, Nombre: {donante[1]}, Grupo Sanguíneo: {donante[7]}, RH: {donante[8]}")
            else:
                print("No se encontraron donantes en la base de datos.")
        except sql.Error as e:
            print("Error al obtener los donantes:", str(e))

        conn.close()
