class Beneficios:
    def __init__(self,idBeneficio,descripcion,idHospital,cantidadSangre,minimoDonaciones):
        self.__idBeneficio = idBeneficio
        self.__descripcion = descripcion
        self.__cantidadSangre = cantidadSangre
        self.__minimoDonaciones = minimoDonaciones
        self.__idHospital = idHospital

        # Setter y Getter para idHospital
    def set_idHospital(self, idHospital):
        self.__idHospital = idHospital

    def get_idHospital(self):
        return self.__idHospital
    

    # Setter y Getter para idBeneficio
    def set_idBeneficio(self, idBeneficio):
        self.__idBeneficio = idBeneficio

    def get_idBeneficio(self):
        return self.__idBeneficio

    # Setter y Getter para descripcion
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion

    # Setter y Getter para cantidadSangre
    def set_cantidadSangre(self, cantidadSangre):
        self.__cantidadSangre = cantidadSangre

    def get_cantidadSangre(self):
        return self.__cantidadSangre

    # Setter y Getter para minimoDonaciones
    def set_minimoDonaciones(self, minimoDonaciones):
        self.__minimoDonaciones = minimoDonaciones

    def get_minimoDonaciones(self):
        return self.__minimoDonaciones