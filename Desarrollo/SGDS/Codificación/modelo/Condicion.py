class Condicion:
    def __init__(self,idCondicion,descripcion,idHospital):
        self.__idCondicion = idCondicion
        self.__descripcion = descripcion
        self.__idHospital = idHospital

    # Setter y Getter para idHospital
    def set_idHospital(self, idHospital):
        self.__idHospital = idHospital

    def get_idHospital(self):
        return self.__idHospital
    
    # Setter y Getter para idCondicion
    def set_idCondicion(self, idCondicion):
        self.__idCondicion = idCondicion

    def get_idCondicion(self):
        return self.__idCondicion

    # Setter y Getter para descripcion
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion
