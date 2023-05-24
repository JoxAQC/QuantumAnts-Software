import random
import string

class Hospital:
    def __init__(self, nombreDeHospital, direccion, telefono, estado, condiciones, beneficios, horarios, credencial):
        self.__idHospital = self.generar_id_aleatorio()
        self.__nombreDeHospital = nombreDeHospital
        self.__direccion = direccion
        self.__telefono = telefono
        self.__estado = estado
        self.__condiciones = condiciones
        self.__beneficios = beneficios
        self.__horarios = horarios
        self.__credencial = credencial

    # Getter para el atributo idHospital
    def get_idHospital(self):
        return self.__idHospital

    # Setter para el atributo idHospital
    def set_idHospital(self, idHospital):
        self.__idHospital = idHospital

    # Getter para el atributo nombreDeHospital
    def get_nombreDeHospital(self):
        return self.__nombreDeHospital

    # Setter para el atributo nombreDeHospital
    def set_nombreDeHospital(self, nombreDeHospital):
        self.__nombreDeHospital = nombreDeHospital

    # Getter para el atributo direccion
    def get_direccion(self):
        return self.__direccion

    # Setter para el atributo direccion
    def set_direccion(self, direccion):
        self.__direccion = direccion

    # Getter para el atributo telefono
    def get_telefono(self):
        return self.__telefono

    # Setter para el atributo telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Getter para el atributo estado
    def get_estado(self):
        return self.__estado

    # Setter para el atributo estado
    def set_estado(self, estado):
        self.__estado = estado

    # Getter para el atributo condiciones
    def get_condiciones(self):
        return self.__condiciones

    # Setter para el atributo condiciones
    def set_condiciones(self, condiciones):
        self.__condiciones = condiciones

    # Getter para el atributo beneficios
    def get_beneficios(self):
        return self.__beneficios

    # Setter para el atributo beneficios
    def set_beneficios(self, beneficios):
        self.__beneficios = beneficios

    # Getter para el atributo horarios
    def get_horarios(self):
        return self.__horarios

    # Setter para el atributo horarios
    def set_horarios(self, horarios):
        self.__horarios = horarios

    # Getter para el atributo credencial
    def get_credencial(self):
        return self.__credencial

    # Setter para el atributo credencial
    def set_credencial(self, credencial):
        self.__credencial = credencial
    
    @staticmethod
    def generar_id_aleatorio():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    
    
    """
    @staticmethod
    def obtener_datos_hospital_por_consola():
        nombreDeHospital = input("Nombre del hospital: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        estado = input("Estado de funcionamiento: ")
        cantidadCondiciones = int(input("Cantidad de condiciones: "))
        condiciones = []
        for _ in range(cantidadCondiciones):
            idCondicion = Hospital.generar_id_aleatorio()
            descripcion = input("Descripción de la condición: ")
            condiciones.append({"idCondicion": idCondicion, "descripcion": descripcion})

        cantidadBeneficios = int(input("Cantidad de beneficios: "))
        beneficios = []
        for _ in range(cantidadBeneficios):
            idBeneficio = Hospital.generar_id_aleatorio()
            descripcion = input("Descripción del beneficio: ")
            cantidadSangre = int(input("Cantidad mínima de sangre donada: "))
            minimoDonaciones = int(input("Mínimo de donaciones realizadas: "))
            beneficios.append({"idBeneficio": idBeneficio, "descripcion": descripcion, "cantidadSangre": cantidadSangre, "minimoDonaciones": minimoDonaciones})

        cantidadHorarios = int(input("Cantidad de horarios de atención: "))
        horarios = []
        for _ in range(cantidadHorarios):
            idHorario = Hospital.generar_id_aleatorio()
            descripcion = input("Descripción del horario de atención: ")
            hora = input("Hora del horario de atención: ")
            horarios.append({"idHorario": idHorario, "descripcion": descripcion, "hora": hora})

        return nombreDeHospital, direccion, telefono, estado, condiciones, beneficios, horarios
    
    
   
    def agregarHospitalBD(self):
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.abspath("")
        # Construir la ruta absoluta del archivo de la base de datos
        db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
        # Establecer la conexión a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        instruction = "INSERT INTO Hospital VALUES (?, ?, ?, ?, ?)"
        cursor.execute(instruction, (self.__idHospital, self.__nombreDeHospital, self.__direccion, self.__telefono, self.__estado))

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

        print("Datos para su credencial: ")
        fechaDeCreacion = date.today().strftime("%Y-%m-%d")
        fechaDeExpiracion = (date.today() + timedelta(days=1825)).strftime("%Y-%m-%d")
        estado = "vigente"
        tipoDeUsuario = "hospital"
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        # Insertar la credencial en la base de datos
        insertar_credencial(self.__idHospital, fechaDeCreacion, fechaDeExpiracion, estado, tipoDeUsuario, username, password)
        
    def registrarHospital():
        # Pedir al usuario un número de licencia
        numero_licencia = input("Ingrese numero de licencia de funcionamiento para registrarse: ")
        # Verificar si el número de licencia está presente en el archivo JSON
        with open("LicenciasVigentesFuncionamiento.json", "r") as archivo_json:
            datos = json.load(archivo_json)
            licencias_vigentes = datos["licencias_vigentes"]
            if numero_licencia in licencias_vigentes:
                print("Licencia validada.Proceda a registrarse: ")
                datos_hospital = Hospital.obtener_datos_hospital_por_consola()
                hospital = Hospital(*datos_hospital)
                hospital.agregarHospitalBD()
                print("Hospital se ha registrado exitosamente y se ha creado su cuenta.")
            else:
                print("La licencia es invalida.")

"""

"""
datos_licencias = {
    "licencias_vigentes": [
        "123456",
        "789012",
        "345678",
        "901234"
    ]
}
"""