import sqlite3 as sql
import os
import tkinter as tk
from tkinter import ttk


class OperacionesHospital:
    def __init__(self, tamaño):
        self.__tamaño = tamaño
    
    def validar_campos_llenos(self, hospital):
        if (
            hospital.get_nombreDeHospital()
            and hospital.get_direccion()
            and hospital.get_telefono()
            and hospital.get_estado()
        ):
            if (
                hospital.get_condiciones()
                and hospital.get_beneficios()
                and hospital.get_horarios()
            ):
                return True
        return False
    
    def agregar_hospital_bd(self, hospital):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Hospital VALUES (?, ?, ?, ?, ?)"
        cursor.execute(instruction, (hospital.get_idHospital(), hospital.get_nombreDeHospital(), hospital.get_direccion(), hospital.get_telefono(), hospital.get_estado()))
            
        for condicion in hospital.get_condiciones():
            id_condicion = condicion.get_idCondicion()
            descripcion = condicion.get_descripcion()
            instruction = "INSERT INTO Condicion VALUES (?, ?, ?)"
            cursor.execute(instruction, (id_condicion, descripcion, hospital.get_idHospital()))

        for beneficio in hospital.get_beneficios():
            id_beneficio = beneficio.get_idBeneficio()
            descripcion = beneficio.get_descripcion()
            cantidad_sangre = beneficio.get_cantidadSangre()
            minimo_donaciones = beneficio.get_minimoDonaciones()
            instruction = "INSERT INTO Beneficio VALUES (?, ?, ?, ?, ?)"
            cursor.execute(instruction, (id_beneficio, descripcion, hospital.get_idHospital(), cantidad_sangre, minimo_donaciones))

        for horario in hospital.get_horarios():
            id_horario = horario.get_idHorario()
            descripcion = horario.get_descripcion()
            hora = horario.get_hora()
            instruction = "INSERT INTO HorarioDeAtencion VALUES (?, ?, ?, ?)"
            cursor.execute(instruction, (id_horario, descripcion, hora, hospital.get_idHospital()))
        
        conn.commit()
        conn.close()

    def modificar_hospital_bd(self, hospital):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "UPDATE Hospital SET nombreDeHospital = ?, direccion = ?, telefono = ?, estado = ? WHERE idHospital = ?"
        cursor.execute(
            instruction,
            (
                hospital.get_nombreDeHospital(),
                hospital.get_direccion(),
                hospital.get_telefono(),
                hospital.get_estado(),
                hospital.get_idHospital(),
            ),
        )

        for condicion in hospital.get_condiciones():
            id_condicion = condicion.get_idCondicion()
            descripcion = condicion.get_descripcion()
            instruction = "UPDATE Condicion SET descripcion = ? WHERE idCondicion = ?"
            cursor.execute(instruction, (descripcion, id_condicion))

        for beneficio in hospital.get_beneficios():
            id_beneficio = beneficio.get_idBeneficio()
            descripcion = beneficio.get_descripcion()
            cantidad_sangre = beneficio.get_cantidadSangre()
            minimo_donaciones = beneficio.get_minimoDonaciones()
            instruction = "UPDATE Beneficio SET descripcion = ?, cantidadSangre = ?, minimoDonaciones = ? WHERE idBeneficio = ?"
            cursor.execute(
                instruction,
                (descripcion, cantidad_sangre, minimo_donaciones, id_beneficio),
            )

        for horario in hospital.get_horarios():
            id_horario = horario.get_idHorario()
            descripcion = horario.get_descripcion()
            hora = horario.get_hora()
            instruction = "UPDATE HorarioDeAtencion SET descripcion = ?, hora = ? WHERE idHorario = ?"
            cursor.execute(instruction, (descripcion, hora, id_horario))

        conn.commit()
        conn.close()

    def buscar_hospital_bd(self, id_hospital):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "SELECT * FROM Hospital WHERE idHospital = ?"
        cursor.execute(instruction, (id_hospital,))
        result = cursor.fetchone()
        conn.close()
        return result

    def eliminar_hospital_bd(self, id_hospital):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "DELETE FROM Hospital WHERE idHospital = ?"
        cursor.execute(instruction, (id_hospital,))
        conn.commit()
        conn.close()

    def ver_hospitales_bd():
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Hospital")
        results = cursor.fetchall()
        conn.close()
        return results

    # Métodos Getter and Setter de tamaño
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def get_tamaño(self):
        return self.__tamaño
    
if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Programa SGDS - Hospitales")

    # Obtener los resultados de la base de datos
    resultados = OperacionesHospital.ver_hospitales_bd()

    # Crear la tabla
    tabla = ttk.Treeview(ventana)

    # Configurar los encabezados de columna
    tabla["columns"] = ("IDHospital", "NombreHospital", "Direccion", "Contacto", "Estado")
    tabla.heading("IDHospital", text="IDHospital")
    tabla.heading("NombreHospital", text="NombreHospital")
    tabla.heading("Direccion", text="Direccion")
    tabla.heading("Contacto", text="Contacto")
    tabla.heading("Estado", text="Estado")

    # Agregar los resultados a la tabla
    for resultado in resultados:
        tabla.insert("", "end", values=resultado)

    # Empacar la tabla
    tabla.pack()

    # Ejecutar la interfaz
    ventana.mainloop()