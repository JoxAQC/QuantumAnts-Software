from Hospital import Hospital
from Credenciales import Credencial
from Condiciones import Condiciones
from Beneficios import Beneficios
from Horarios import Horarios
import sqlite3 as sql
import os
import json

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
    
    credencial = Credencial(1, "12/02/2024","12/02/2025", "Activo", "Donante", 
                "RogelioElCrag", "1234")
    horariolista = list()
    horario1 = Horarios(1, "Horario 1", "08:00",1)
    horario2 = Horarios(2, "Horario 2", "12:00",1)
    horario3 = Horarios(3, "Horario 3", "16:00",1)
    horariolista.append(horario1)
    horariolista.append(horario2)
    horariolista.append(horario3)
    condicionesLista = list()
    condicion1 = Condiciones(1,"nose",1)
    condicionesLista.append(condicion1)
    beneficiosLista = list()
    beneficio1 = Beneficios(1,"nose",1,1,1)
    beneficiosLista.append(beneficio1)
    hospital = Hospital(1,"Maria Auxiliadora", "Las Perlas #524", "987654321", 
                    "Activo", condicionesLista,beneficiosLista, horariolista, credencial)
    numeroLicencia="123456"
    Sistema.registrarHospital(hospital,credencial,numeroLicencia)
 
if __name__=="__main__":
    mainR1()