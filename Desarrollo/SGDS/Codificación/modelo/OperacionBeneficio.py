import os
import sqlite3 as sql

class OperacionBeneficio:
    def __init__(self):
        pass
    
    def ver_beneficios_obtenidos(self, donante):
        conn = donante.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM beneficios WHERE idDonante = ?", (donante.get_id_donante(),)
            )
            beneficios = cursor.fetchall()

            if len(beneficios) > 0:
                print("Beneficios obtenidos:")
                for beneficio in beneficios:
                    print(f"Fecha: {beneficio[1]}, Descripción: {beneficio[2]}")
            else:
                print("No se han obtenido beneficios.")
        except sql.Error as e:
            print("Error al obtener los beneficios:", str(e))

        conn.close()

    def agregar_grupo_beneficios(self, hospital, grupo_beneficios):
        conn = hospital.conectar_bd()
        cursor = conn.cursor()

        try:
            for beneficio in grupo_beneficios:
                cursor.execute(
                    "INSERT INTO beneficios (fecha, descripcion, idHospital) VALUES (?, ?, ?)",
                    (beneficio["fecha"], beneficio["descripcion"], hospital.get_id_hospital()),
                )

            conn.commit()
            print("Grupo de beneficios agregado exitosamente.")
        except sql.Error as e:
            print("Error al agregar el grupo de beneficios:", str(e))

        conn.close()

    def eliminar_beneficio(self, hospital, beneficio_id):
        conn = hospital.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM beneficios WHERE idBeneficio = ?", (beneficio_id,))

            conn.commit()
            print("Beneficio eliminado exitosamente.")
        except sql.Error as e:
            print("Error al eliminar el beneficio:", str(e))

        conn.close()

    def modificar_beneficio(self, hospital, beneficio_id, nueva_descripcion):
        conn = hospital.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE beneficios SET descripcion = ? WHERE idBeneficio = ?",
                (nueva_descripcion, beneficio_id),
            )

            conn.commit()
            print("Beneficio modificado exitosamente.")
        except sql.Error as e:
            print("Error al modificar el beneficio:", str(e))

        conn.close()

    def buscar_beneficios(self, hospital, descripcion):
        conn = hospital.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM beneficios WHERE descripcion LIKE ?",
                (f"%{descripcion}%",)
            )

            beneficios = cursor.fetchall()

            return beneficios
        except sql.Error as e:
            print("Error al buscar beneficios:", str(e))

        conn.close()
        return []

    def ver_beneficios_hospital(self, hospital):
        conn = hospital.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM beneficios WHERE idHospital = ?", (hospital.get_id_hospital(),)
            )
            beneficios = cursor.fetchall()

            if len(beneficios) > 0:
                print("Beneficios del hospital:")
                for beneficio in beneficios:
                    print(f"Fecha: {beneficio[1]}, Descripción: {beneficio[2]}")
            else:
                print("El hospital no tiene beneficios.")
        except sql.Error as e:
            print("Error al obtener los beneficios del hospital:", str(e))

        conn.close()

    def validarBeneficio(self,beneficio):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Obtener el beneficio correspondiente al idBeneficio proporcionado
        select_instruction = "SELECT * FROM Beneficio WHERE idBeneficio = ?"
        cursor.execute(select_instruction, (beneficio.get_idBeneficio(),))
        result = cursor.fetchone()

        if result:
            # Comparar los valores de cantidadSngre y minimoDonacion con los del beneficio proporcionado
            id_beneficio, descripcion, id_hospital, cantidad_sangre, minimo_donacion = result
            if cantidad_sangre == beneficio.get_cantidadSangre() and minimo_donacion == beneficio.get_minimoDonaciones():
                conn.close()
                return True  # El beneficio es válido
        conn.close()
        return False  # El beneficio no es válido
