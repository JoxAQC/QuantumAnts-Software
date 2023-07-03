import sqlite3 as sql

def createDB():
    conn = sql.connect("SGDS-VABD01.db")
    conn.commit()
    conn.close()

def createTableHospital():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Hospital(
         idHospital integer,
         nombreDeHospital text,
         descripcionHospital text,
         direccion text,
         telefono text,
         estado integer
        )"""   
    )
    conn.commit()
    conn.close()

def insertRowHospital(idHospital,nombreDeHospital,descripcionHospital,direccion,telefono,estado):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Hospital VALUES ({idHospital},'{nombreDeHospital}','{descripcionHospital}','{direccion}','{telefono}',{estado})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowCondicion(idCondicion,descripcion,idHospital):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Condicion VALUES ({idCondicion},'{descripcion}',{idHospital})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowHorarioDeAtencion(idHorario,descripcion,hora,idHospital):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO HorarioDeAtencion VALUES ({idHorario},'{descripcion}','{hora}',{idHospital})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def insertRowBeneficio(idBeneficio,descripcion,idHospital,cantidadSangre,minimoDonaciones):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Beneficio VALUES ({idBeneficio},'{descripcion}',{idHospital},{cantidadSangre},{minimoDonaciones})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowCredencial(idCredencial,fechaDeCreacion,fechaDeExpiracion,estado,tipoDeUsuario,user,password):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Credencial VALUES ({idCredencial},'{fechaDeCreacion}','{fechaDeExpiracion}',{estado},'{tipoDeUsuario}','{user}','{password}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowDonante(idDonante,nombre,fechaNacimiento,dni,telefono,direccion,beneficioActivo,grupoSanguineo,RH,ultimaDonacion,idHospitalUltimo):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Donante VALUES ({idDonante},'{nombre}','{fechaNacimiento}','{dni}','{telefono}','{direccion}','{beneficioActivo}','{grupoSanguineo}','{RH}','{ultimaDonacion}',{idHospitalUltimo})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def insertRowCita(idCita,fecha,idDonante,idHospital,estado):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Cita VALUES ({idCita},'{fecha}',{idDonante},{idHospital},{estado})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def createTableCondicion():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Condicion(
         idCondicion integer,
         descripcion text,
         idHospital integer
        )"""   
    )
    conn.commit()
    conn.close()

def createTableHorarioDeAtencion():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE HorarioDeAtencion(
         idHorario integer,
         desripcion text,
         hora text,
         idHospital integer
        )"""   
    )
    conn.commit()
    conn.close()

def createTableBeneficio():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Beneficio(
         idBeneficio integer,
         desripcion text,
         idHospital integer,
         cantidadSangre integer,
         minimoDonaciones integer
        )"""
       
    )
    conn.commit()
    conn.close()

def createTableCredencial():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Credencial(
         idCredencial integer,
         fechaDeCreacion text,
         fechaDeExpiracion text,
         estado integer,
         tipoDeUsuario text,
         user text,
         password text
        )"""   
    )
    conn.commit()
    conn.close()

def createTableDonante():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Donante(
         idDonante integer,
         nombre text,
         fechaNacimiento text,
         dni text,
         telefono text,
         direccion text,
         beneficioActivo text,
         grupoSanguineo text,
         RH text,
         ultimaDonacion text,
         idHospitalUltimo integer
        )"""   
    )
    conn.commit()
    conn.close()


def createTableCita():
    conn=sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Cita(
         idCita integer,
         fecha text,
         idDonante integer,
         idHospital integer,
         estado integer
        )"""   
    )
    conn.commit()
    conn.close()

def limpiarTable(tabla):
    conn = sql.connect("SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM   {}
        """.format(tabla)
    )
    conn.commit()
    conn.close()
