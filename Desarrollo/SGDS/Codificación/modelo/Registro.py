from Credencial import Credencial
from Hospital import Hospital
import os
import sqlite3 as sql
import json

class Registro:
    def __init__(self, estado):
        self.__estado = estado
    
    # Getter para el atributo estado
    def get_estado(self):
        return self.__estado

    # Setter para el atributo estado
    def set_estado(self, estado):
        self.__estado = estado
        
    #Registro del credencial
    def insertar_credencial(self, credencial):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instruction, (Credencial.get_idCredencial, Credencial.get_fechaDeCreacionCredencial, 
                                     Credencial.get_fechaDeExpiracion, Credencial.get_estadoCredencial,
                                     Credencial.get_tipoDeUsuarioCredencial, Credencial.get_usernameCredencial,
                                     Credencial.get_passwordCredencial))
        conn.commit()
        conn.close() 
    
    def agregarHospitalBD(self):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Hospital VALUES (?, ?, ?, ?, ?)"
        cursor.execute(instruction, (Hospital.get_idHospital, Hospital.get_nombreDeHospital, 
                                     Hospital.get_direccion, Hospital.get_telefono, Hospital.get_estado))

        for condicion in self.__condiciones:
            idCondicion = condicion["idCondicion"]
            descripcion = condicion["descripcion"]
            instruction = "INSERT INTO Condicion VALUES (?, ?, ?)"
            cursor.execute(instruction, (idCondicion, descripcion, self.__idHospital))

        for beneficio in self.__beneficios:
            idBeneficio = beneficio["idBeneficio"]
            descripcion = beneficio["descripcion"]
            cantidadSangre = beneficio["cantidadSangre"]
            minimoDonaciones = beneficio["minimoDonaciones"]
            instruction = "INSERT INTO Beneficio VALUES (?, ?, ?, ?, ?)"
            cursor.execute(instruction, (idBeneficio, descripcion, self.__idHospital, cantidadSangre, minimoDonaciones))

        for horario in self.__horarios:
            idHorario = horario["idHorario"]
            descripcion = horario["descripcion"]
            hora = horario["hora"]
            instruction = "INSERT INTO HorarioDeAtencion VALUES (?, ?, ?, ?)"
            cursor.execute(instruction, (idHorario, descripcion, hora, self.__idHospital))
        
        conn.commit()
        conn.close()