import sqlite3 as sql
import os

def buscar_donantes(donante, grupo_sanguineo, ubicacion):
    conn = donante.conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM Donante WHERE grupo_sanguineo = ? AND direccion LIKE ?",
            (grupo_sanguineo, f"%{ubicacion}%"),
        )

        donantes = cursor.fetchall()

        return donantes
    except sql.Error as e:
        print("Error al buscar donantes:", str(e))

    conn.close()
    return []


def verCitas(donante):
    conn = donante.conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM citas WHERE idDonante = ?", (donante.idDonante,))
        citas = cursor.fetchall()

        if len(citas) > 0:
            print("Citas:")
            for cita in citas:
                print(f"Fecha: {cita[1]}, Hospital: {cita[2]}")
        else:
            print("No hay citas programadas.")
    except sql.Error as e:
        print("Error al obtener las citas:", str(e))

    conn.close()


def verBeneficiosObtenidos(donante):
    conn = donante.conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM beneficios WHERE idDonante = ?", (donante.idDonante,)
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


def cambiarDatos(donante, nombre, fechaNacimiento, dni, telefono, direccion):
    donante.nombre = nombre
    donante.fechaNacimiento = fechaNacimiento
    donante.dni = dni
    donante.telefono = telefono
    donante.direccion = direccion

    conn = donante.conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE Donante SET nombre = ?, fecha_nacimiento = ?, dni = ?, telefono = ?, "
            "direccion = ? WHERE idDonante = ?",
            (
                donante.nombre,
                donante.fechaNacimiento,
                donante.dni,
                donante.telefono,
                donante.direccion,
                donante.idDonante,
            ),
        )

        conn.commit()
        print("Datos actualizados exitosamente.")
    except sql.Error as e:
        print("Error al actualizar los datos:", str(e))

    conn.close()

    def confirmarCita(cita):
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
    
    def finalizarCita(cita):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        instruction = "DELETE FROM Credencial WHERE idCita = ?"
        cursor.execute(instruction, (cita.get_idCita(),))
        conn.commit()

        conn.close()
    
    def programarCita(donante, horario):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        id_donante = donante.get_idDonante()
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

    def reprogramarCita(cita, fechaNueva):
        current_dir = os.path.abspath("")
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        id_cita = cita.get_idCita()

        instruction = "UPDATE Credencial SET fecha = ? WHERE idCita = ?"
        cursor.execute(instruction, (fechaNueva, id_cita))
        conn.commit()

        conn.close()  
