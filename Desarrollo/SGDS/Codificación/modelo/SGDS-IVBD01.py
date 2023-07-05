import sqlite3 as sql


def createDB():
    conn = sql.connect("modelo/SGDS-VABD01.db")
    conn.commit()
    conn.close()

def createTableHospital():
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Hospital VALUES ({idHospital},'{nombreDeHospital}','{descripcionHospital}','{direccion}','{telefono}',{estado})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowCondicion(idCondicion,descripcion,idHospital):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Condicion VALUES ({idCondicion},'{descripcion}',{idHospital})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowHorarioDeAtencion(idHorario,descripcion,hora,idHospital):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO HorarioDeAtencion VALUES ({idHorario},'{descripcion}','{hora}',{idHospital})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def insertRowBeneficio(idBeneficio,descripcion,idHospital,cantidadSangre,minimoDonaciones):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Beneficio VALUES ({idBeneficio},'{descripcion}',{idHospital},{cantidadSangre},{minimoDonaciones})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowCredencial(idCredencial,fechaDeCreacion,fechaDeExpiracion,estado,tipoDeUsuario,user,password):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Credencial VALUES ({idCredencial},'{fechaDeCreacion}','{fechaDeExpiracion}',{estado},'{tipoDeUsuario}','{user}','{password}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def insertRowDonante(idDonante,nombre,fechaNacimiento,dni,telefono,direccion,beneficioActivo,grupoSanguineo,RH,ultimaDonacion,idHospitalUltimo):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Donante VALUES ({idDonante},'{nombre}','{fechaNacimiento}','{dni}','{telefono}','{direccion}','{beneficioActivo}','{grupoSanguineo}','{RH}','{ultimaDonacion}',{idHospitalUltimo})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def insertRowCita(idCita,fecha,idDonante,idHospital,estado):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Cita VALUES ({idCita},'{fecha}',{idDonante},{idHospital},{estado})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def createTableCondicion():
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn=sql.connect("modelo/SGDS-VABD01.db")
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
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM   {}
        """.format(tabla)
    )
    conn.commit()
    conn.close()

#insertRowHospital(1234,"Hospital Nacional Cayetano Heredia","Nuestro Hospital en su corta existencia es reconocido como líder nacional por su aporte al país en tecnología, generación de programas de salud y formación de profesionales y técnicos. Actualmente el Hospital cuenta con un área de influencia de aproximadamente 3`000,000 personas que significan seis veces más el número de personas que se preveía en 1968 y superando las dificultades que se presentan en el día a día. El hospital Nacional Cayetano Heredia siempre ha tenido a la vista un ideal de excelencia en su triple actividad: asistencial, docente y de investigación.","Av. Honorio Delgado 262, San Martín de Porres 15102","(01) 4820402",1)
#insertRowCredencial(1234,"05-07-2023","05-07-2027",1,"Hospital","cayetano1","cayetano123")
#insertRowHorarioDeAtencion(12341,"Matutino","08:00-10:00",1234)
#insertRowCondicion(12341,"Mayor de 18 años.",1234)
#insertRowBeneficio(12341,"Consulta dermatologica gratis.",1234,1,1)

#insertRowHospital(5678,"Hospital Edgardo Rebagliati Martins","El Hospital Nacional Edgardo Rebagliati Martins, antiguo Hospital del Empleado, es un centro hospitalario público peruano situado en Lima y administrado por EsSalud. Es el más importante complejo hospitalario de la seguridad social del Perú.​","Av. Edgardo Rebagliati 490, Jesús María 15072","(01) 2654901",1)
#insertRowCredencial(5678,"05-07-2023","05-07-2027",1,"Hospital","edgardoR1","edgardoR123")
#insertRowHorarioDeAtencion(56781,"Matutino","09:00-10:00",5678)
#insertRowCondicion(56781,"Mayor de 22 años.",5678)
#insertRowBeneficio(56781,"Consulta cardiologica gratis.",5678,1,1)

#insertRowHospital(9101,"Hospital Nacional Dos De Mayo","El Hospital Nacional Dos de Mayo es el primer centro hospitalario público peruano administrado por el Ministerio de Salud del Perú, considerado como el primer hospital del Perú republicano.","Parque Historia de la Medicina Peruana, S/N, Av. Miguel Grau 13, Lima 15003","(01) 3280028",1)
#insertRowCredencial(9101,"05-07-2023","05-07-2027",1,"Hospital","dosmayo1","dosmayo123")
#insertRowHorarioDeAtencion(91011,"Nocturno","18:00-22:00",9101)
#insertRowCondicion(91011,"Mayor de 19 años.",9101)
#insertRowBeneficio(91011,"Consulta oncologica gratis.",9101,1,1)


