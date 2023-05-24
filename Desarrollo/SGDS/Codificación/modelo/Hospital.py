class Hospital:
    def __init__(self, idHospital,nombreDeHospital, direccion, telefono, estado, condiciones, beneficios, horarios,credencial):
        self.__idHospital = idHospital
        self.__nombreDeHospital = nombreDeHospital
        self.__direccion = direccion
        self.__telefono = telefono
        self.__estado = estado
        self.__condiciones = condiciones
        self.__beneficios = beneficios
        self.__horarios = horarios
        self.__credencial = credencial

    # Setter y Getter para idHospital
    def set_idHospital(self, idHospital):
        self.__idHospital = idHospital

    def get_idHospital(self):
        return self.__idHospital

    # Setter y Getter para nombreDeHospital
    def set_nombreDeHospital(self, nombreDeHospital):
        self.__nombreDeHospital = nombreDeHospital

    def get_nombreDeHospital(self):
        return self.__nombreDeHospital

    # Setter y Getter para direccion
    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_direccion(self):
        return self.__direccion

    # Setter y Getter para telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_telefono(self):
        return self.__telefono

    # Setter y Getter para estado
    def set_estado(self, estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    # Setter y Getter para condiciones
    def set_condiciones(self, condiciones):
        self.__condiciones = condiciones

    def get_condiciones(self):
        return self.__condiciones

    # Setter y Getter para beneficios
    def set_beneficios(self, beneficios):
        self.__beneficios = beneficios

    def get_beneficios(self):
        return self.__beneficios

    # Setter y Getter para horarios
    def set_horarios(self, horarios):
        self.__horarios = horarios

    def get_horarios(self):
        return self.__horarios


#datos_licencias = {
#    "licencias_vigentes": [
#        "123456",
#        "789012",
#        "345678",
#        "901234"
#    ]
#}
