from Hospital import Hospital
from Credenciales import Credencial
from Condiciones import Condiciones
from Beneficios import Beneficios
from Horarios import Horarios
from Cita import Cita
from HorarioDeAtencion import HorarioDeAtencion
import sqlite3 as sql
import os
import json
import random
from datetime import datetime, timedelta

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

    def confirmarCita(self, cita):
        # Verificar y confirmar una cita en la base de datos
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Verificar el estado actual de la cita en la base de datos
        cursor.execute("SELECT estado FROM Cita WHERE idCita = ?", (cita.get_idCita(),))
        result = cursor.fetchone()
        if result is not None:
            estado_actual = result[0]
            if estado_actual == 0:  # Si el estado actual es 0 (False)
                # Actualizar el estado de la cita en la base de datos a 1 (True)
                cursor.execute("UPDATE Cita SET estado = 1 WHERE idCita = ?", (cita.get_idCita(),))
                conn.commit()
                conn.close()
                return True
        conn.close()
        return False
    
    def programarCita(self, donante, hora):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Obtener la fecha para programar la cita (día siguiente)
        fecha = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        # Obtener el idCita siguiente disponible
        instruction = "SELECT MAX(idCita) FROM Cita"
        cursor.execute(instruction)
        result = cursor.fetchone()
        if result[0] is not None:
            idCita = result[0] + 1
        else:
            idCita = 1

        # Crear una instancia de la clase Cita
        cita = Cita(idCita, fecha, donante, hora)

        try:
            # Guardar la cita en la base de datos
            instruction = "INSERT INTO Cita VALUES (?, ?, ?, ?, ?)"
            cursor.execute(instruction, (idCita, fecha, donante.idDonante, hora.idHorario, True))
            conn.commit()
            conn.close()
            return True  # La cita se programó correctamente
        except Exception as e:
            print("Error al programar la cita:", str(e))
            conn.rollback()
            conn.close()
            return False  # Error al programar la cita

    def reprogramarCita(self, fechanueva):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Obtener la cita activa
        instruction = "SELECT * FROM Cita WHERE estado = 1"
        cursor.execute(instruction)
        row = cursor.fetchone()

        if row is not None:
            # Actualizar la fecha de la cita
            idCita = row[0]
            fecha = fechanueva.strftime("%Y-%m-%d %H:%M:%S")
            instruction = "UPDATE Cita SET fecha = ? WHERE idCita = ?"
            cursor.execute(instruction, (fecha, idCita))
            conn.commit()
            conn.close()

            return True  # La cita se reprogramó exitosamente

        conn.close()
        return False  # No se encontró una cita activa
    def finalizarCita(self, donante):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        try:
            # Eliminar la cita del donante en la base de datos
            instruction = "DELETE FROM Cita WHERE idDonante = ?"
            cursor.execute(instruction, (donante.idDonante,))
            conn.commit()
            conn.close()
            return True  # La cita se eliminó correctamente
        except Exception as e:
            print("Error al finalizar la cita:", str(e))
            conn.rollback()
            conn.close()
            return False  # Error al finalizar la cita    


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

