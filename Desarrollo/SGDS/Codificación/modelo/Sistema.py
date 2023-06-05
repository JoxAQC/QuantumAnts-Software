from Hospital import Hospital
from Credenciales import Credencial
from Condiciones import Condiciones
from Beneficios import Beneficios
from Horarios import Horarios
from Cita import Cita
import sqlite3 as sql
import os
import json
import random
from datetime import datetime, timedelta

class Sistema:
    def __init__(self, estado):
        self.__estado = estado

    def validar_campos_llenos(hospital):
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
        if Sistema.validar_campos_llenos(hospital):
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
        else:
            print("Datos ingresados incorrectamente o vacios.")

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

def mainR1():
         
    #datos_licencias = {
    #"licencias_vigentes": [
    #    "123456",
    #    "789012",
    #    "345678",
    #    "901234"
    #]
    #}
    # Escribir datos en el archivo JSON
    #with open("LicenciasVigentesFuncionamiento.json", "w") as archivo:
    #    json.dump(datos_licencias, archivo)

    idHospitalyCredencial = Sistema.generar_id_credencial()
    credencial = Credencial(idHospitalyCredencial, "12/02/2024","12/02/2025", "Activo", "Donante", 
                "RogelioElCrag", "1234")
    horariolista = list()
    horario1 = Horarios(1, "Horario 1", "08:00",idHospitalyCredencial)
    horario2 = Horarios(2, "Horario 2", "12:00",idHospitalyCredencial)
    horario3 = Horarios(3, "Horario 3", "16:00",idHospitalyCredencial)
    horariolista.append(horario1)
    horariolista.append(horario2)
    horariolista.append(horario3)
    condicionesLista = list()
    condicion1 = Condiciones(1,"nose",idHospitalyCredencial)
    condicionesLista.append(condicion1)
    beneficiosLista = list()
    beneficio1 = Beneficios(1,"nose",idHospitalyCredencial,1,1)
    beneficiosLista.append(beneficio1)
    hospital = Hospital(idHospitalyCredencial,"Maria Auxiliadora", "Las Perlas #524", "987654321", 
                    "Activo", condicionesLista,beneficiosLista, horariolista, credencial)
    numeroLicencia="123456"
    Sistema.registrarHospital(hospital,credencial,numeroLicencia)
   
if __name__=="__main__":
   mainR1()

