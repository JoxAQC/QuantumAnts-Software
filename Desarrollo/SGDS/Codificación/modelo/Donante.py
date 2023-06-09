class Donante:
    def __init__(self, id_donante, nombre, fecha_nacimiento, dni, telefono, 
                 direccion, beneficio_activo, grupo_sanguineo, rh, 
                 ultima_donacion, id_hospital_ultimo):
        self.__id_donante = id_donante
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__dni = dni
        self.__telefono = telefono
        self.__direccion = direccion
        self.__beneficio_activo = beneficio_activo
        self.__grupo_sanguineo = grupo_sanguineo
        self.__rh = rh
        self.__ultima_donacion = ultima_donacion
        self.__id_hospital_ultimo = id_hospital_ultimo

    # Getter y Setter para  idDonantes
    def get_id_donante(self):
        return self.__id_donante

    def set_id_donante(self, id_donante):
        self.__id_donante = id_donante

    # Getter y Setter para nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter y Setter para fechaNacimiento
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    # Getter y Setter para dni
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    # Getter y Setter para  telefono
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Getter y Setter para direccion
    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # Getter y Setter para beneficioActivo
    def get_beneficio_activo(self):
        return self.__beneficio_activo

    def set_beneficio_activo(self, beneficio_activo):
        self.__beneficio_activo = beneficio_activo

    # Getter y Setter para grupoSanguineo
    def get_grupo_sanguineo(self):
        return self.__grupo_sanguineo

    def set_grupo_sanguineo(self, grupo_sanguineo):
        self.__grupo_sanguineo = grupo_sanguineo

    # Getter y Setter para RH
    def get_rh(self):
        return self.__rh

    def set_rh(self, rh):
        self.__rh = rh

    # Getter y Setter para ultimaDonacion
    def get_ultima_donacion(self):
        return self.__ultima_donacion

    def set_ultima_donacion(self, ultima_donacion):
        self.__ultima_donacion = ultima_donacion

    # Getter y Setter para id HospitalUltimo
    def get_id_hospitalUltimo(self):
        return self.__id_hospital_ultimo

    def set_idHospitalUltimo(self, id_hospital_ultimo):
        self.__id_hospital_ultimo = id_hospital_ultimo