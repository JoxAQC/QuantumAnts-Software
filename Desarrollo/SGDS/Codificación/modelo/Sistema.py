from Hospital import Hospital
from Credenciales import Credencial
from Condiciones import Condiciones
from Beneficios import Beneficios
from Horarios import Horarios
from Donante import Donante
import sqlite3 as sql
import os
import json
import random


class Sistema:
    def __init__(self, estado):
        self.__estado = estado

    def registrar_credencial(credencial):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instruction, (credencial.get_idCredencial(), credencial.get_fechaDeCreacion(), credencial.get_fechaDeExpiracion(), credencial.get_estado(), credencial.get_tipoDeUsuario(), credencial.get_username(), credencial.get_password()))
        conn.commit()
        conn.close()

    def agregarHospitalBD(hospital): #hospital = Hospital("","","","")
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Hospital VALUES (?, ?, ?, ?, ?)"
        cursor.execute(instruction, (hospital.get_idHospital(), hospital.get_nombreDeHospital(), hospital.get_direccion(), hospital.get_telefono(), hospital.get_estado()))

        for condicion in hospital.get_condiciones():
            idCondicion = condicion.get_idCondicion()
            descripcion = condicion.get_descripcion()
            instruction = "INSERT INTO Condicion VALUES (?, ?, ?)"
            cursor.execute(instruction, (idCondicion, descripcion, hospital.get_idHospital()))

        for beneficio in hospital.get_beneficios():
            idBeneficio = beneficio.get_idBeneficio()
            descripcion = beneficio.get_descripcion()
            cantidadSangre = beneficio.get_cantidadSangre()
            minimoDonaciones = beneficio.get_minimoDonaciones()
            instruction = "INSERT INTO Beneficio VALUES (?, ?, ?, ?, ?)"
            cursor.execute(instruction, (idBeneficio, descripcion, hospital.get_idHospital(), cantidadSangre, minimoDonaciones))

        for horario in hospital.get_horarios():
            idHorario = horario.get_idHorario()
            descripcion = horario.get_descripcion()
            hora = horario.get_hora()
            instruction = "INSERT INTO HorarioDeAtencion VALUES (?, ?, ?, ?)"
            cursor.execute(instruction, (idHorario, descripcion, hora, hospital.get_idHospital()))

        conn.commit()
        conn.close()

    #hospital = Hospital("""""""""",[],[],[])
    def registrarHospital(hospital,credencial,numeroLicencia):
        # Verificar si el número de licencia está presente en el archivo JSON
        with open("LicenciasVigentesFuncionamiento.json", "r") as archivo_json:
            datos = json.load(archivo_json)
            licencias_vigentes = datos["licencias_vigentes"]
            if numeroLicencia in licencias_vigentes:
                Sistema.registrar_credencial(credencial)
                # Agregar hospital a la base de datos
                Sistema.agregarHospitalBD(hospital)
                print("Hospital se ha registrado exitosamente y se ha creado su cuenta.")
            else:
                print("La licencia es inválida.")

    def generar_id_credencial():
        # Genera un número entero aleatorio de 7 dígitos
        id_credencial = random.randint(1000000, 9999999)
        return id_credencial

    ##########
    def conectar_bd():  
        # Obtener la ruta absoluta al archivo de base de datos
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

        # Establecer conexión con la base de datos
        conn = sql.connect(db_path)
        return conn

    def registrar_donante(donante):
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
                    donante.get_idDonante(),
                    donante.get_nombre(),
                    donante.get_fechaNacimiento(),
                    donante.get_dni(),
                    donante.get_telefono(),
                    donante.get_direccion(),
                    donante.get_beneficioActivo(),
                    donante.get_grupoSanguineo(),
                    donante.get_RH(),
                    donante.get_ultimaDonacion(),
                    donante.get_idHospitalUltimo(),
                ),
            )

            conn.commit()
            print("Donante registrado exitosamente.")
        except sql.Error as e:
            print("Error al registrar el donante:", str(e))

        conn.close()


    def buscar_donantes(self, grupo_sanguineo, ubicacion):
        conn = self.conectar_bd()
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

    def verCitas(self):
        conn = self.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM citas WHERE idDonante = ?", (self.idDonante,))
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

    def verBeneficiosObtenidos(self):
        conn = self.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM beneficios WHERE idDonante = ?", (self.idDonante,)
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


    def cambiarDatos(self, nombre, fechaNacimiento, dni, telefono, direccion):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion

        conn = self.conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE Donante SET nombre = ?, fecha_nacimiento = ?, dni = ?, telefono = ?, "
                "direccion = ? WHERE idDonante = ?",
                (
                    self.nombre,
                    self.fechaNacimiento,
                    self.dni,
                    self.telefono,
                    self.direccion,
                    self.idDonante,
                ),
            )

            conn.commit()
            print("Datos actualizados exitosamente.")
        except sql.Error as e:
            print("Error al actualizar los datos:", str(e))

        conn.close()