class Donante:
    def __init__(self, idDonante, nombre, fechaNacimiento, dni, telefono, direccion, beneficioActivo, grupoSanguineo, RH, ultimaDonacion, idHospitalUltimo):
        self.__idDonante = idDonante
        self.__nombre = nombre
        self.__fechaNacimiento = fechaNacimiento
        self.__dni = dni
        self.__telefono = telefono
        self.__direccion = direccion
        self.__beneficioActivo = beneficioActivo
        self.__grupoSanguineo = grupoSanguineo
        self.__RH = RH 
        self.__ultimaDonacion = ultimaDonacion
        self.__idHospitalUltimo = idHospitalUltimo

    def get_idDonante(self):
        return self.__idDonante

    def set_idDonante(self, idDonante):
        self.__idDonante = idDonante

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_fechaNacimiento(self):
        return self.__fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_beneficioActivo(self):
        return self.__beneficioActivo

    def set_beneficioActivo(self, beneficioActivo):
        self.__beneficioActivo = beneficioActivo

    def get_grupoSanguineo(self):
        return self.__grupoSanguineo

    def set_grupoSanguineo(self, grupoSanguineo):
        self.__grupoSanguineo = grupoSanguineo

    def get_RH(self):
        return self.__RH

    def set_RH(self, RH):
        self.__RH = RH

    def get_ultimaDonacion(self):
        return self.__ultimaDonacion

    def set_ultimaDonacion(self, ultimaDonacion):
        self.__ultimaDonacion = ultimaDonacion

    def get_idHospitalUltimo(self):
        return self.__idHospitalUltimo

    def set_idHospitalUltimo(self, idHospitalUltimo):
        self.__idHospitalUltimo = idHospitalUltimo