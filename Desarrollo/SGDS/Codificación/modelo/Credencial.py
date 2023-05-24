class Credencial:
    def __init__(self, idCredencial, fechaDeCreacionCredencial, fechaDeExpiracion, estadoCredencial, tipoDeUsuarioCredencial, usernameCredencial, passwordCredencial):
        self.__idCredencial = idCredencial
        self.__fechaDeCreacionCredencial = fechaDeCreacionCredencial
        self.__fechaDeExpiracion = fechaDeExpiracion
        self.__estadoCredencial = estadoCredencial
        self.__tipoDeUsuarioCredencial = tipoDeUsuarioCredencial
        self.__usernameCredencial = usernameCredencial
        self.__passwordCredencial = passwordCredencial
    
    # Getter para el atributo idCredencial
    def get_idCredencial(self):
        return self.__idCredencial
    
    # Setter para el atributo idCredencial
    def set_idCredencial(self, idCredencial):
        self.__idCredencial = idCredencial
    
    # Getter para el atributo fechaDeCreacionCredencial
    def get_fechaDeCreacionCredencial(self):
        return self.__fechaDeCreacionCredencial
    
    # Setter para el atributo fechaDeCreacionCredencial
    def set_fechaDeCreacionCredencial(self, fechaDeCreacionCredencial):
        self.__fechaDeCreacionCredencial = fechaDeCreacionCredencial
    
    # Getter para el atributo fechaDeExpiracion
    def get_fechaDeExpiracion(self):
        return self.__fechaDeExpiracion
    
    # Setter para el atributo fechaDeExpiracion
    def set_fechaDeExpiracion(self, fechaDeExpiracion):
        self.__fechaDeExpiracion = fechaDeExpiracion
    
    # Getter para el atributo estadoCredencial
    def get_estadoCredencial(self):
        return self.__estadoCredencial
    
    # Setter para el atributo estadoCredencial
    def set_estadoCredencial(self, estadoCredencial):
        self.__estadoCredencial = estadoCredencial
    
    # Getter para el atributo tipoDeUsuarioCredencial
    def get_tipoDeUsuarioCredencial(self):
        return self.__tipoDeUsuarioCredencial
    
    # Setter para el atributo tipoDeUsuarioCredencial
    def set_tipoDeUsuarioCredencial(self, tipoDeUsuarioCredencial):
        self.__tipoDeUsuarioCredencial = tipoDeUsuarioCredencial
    
    # Getter para el atributo usernameCredencial
    def get_usernameCredencial(self):
        return self.__usernameCredencial
    
    # Setter para el atributo usernameCredencial
    def set_usernameCredencial(self, usernameCredencial):
        self.__usernameCredencial = usernameCredencial
    
    # Getter para el atributo passwordCredencial
    def get_passwordCredencial(self):
        return self.__passwordCredencial
    
    # Setter para el atributo passwordCredencial
    def set_passwordCredencial(self, passwordCredencial):
        self.__passwordCredencial = passwordCredencial