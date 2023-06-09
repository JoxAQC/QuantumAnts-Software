class Horario:
    def __init__(self,idHorario,descripcion,hora,idHospital):
        self.__idHorario = idHorario
        self.__descripcion = descripcion
        self.__hora = hora
        self.__idHospital = idHospital

    # Setter y Getter para idHorario
    def set_idHorario(self, idHorario):
        self.__idHorario = idHorario

    def get_idHorario(self):
        return self.__idHorario
    
    # Setter y Getter para idHospital
    def set_idHospital(self, idHospital):
        self.__idHospital = idHospital

    def get_idHospital(self):
        return self.__idHospital

    # Setter y Getter para descripcion
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion

    # Setter y Getter para hora
    def set_hora(self, hora):
        self.__hora = hora

    def get_hora(self):
        return self.__hora