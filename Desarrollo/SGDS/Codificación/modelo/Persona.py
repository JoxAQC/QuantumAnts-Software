class Persona:
    def __init__(self, nombre, edad, fecha_nacimiento, comida_favorita):
        self.__nombre = nombre
        self.__edad = edad
        self.__fecha_nacimiento = fecha_nacimiento
        self.__comida_favorita = comida_favorita

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_comida_favorita(self):
        return self.__comida_favorita

    def set_edad(self, edad):
        self.__edad = edad

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_comida_favorita(self, comida_favorita):
        self.__comida_favorita = comida_favorita
