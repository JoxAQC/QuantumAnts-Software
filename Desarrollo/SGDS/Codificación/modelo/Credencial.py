class Credencial:
    def __init__(self, idCredencial, fechaDeCreacion, fechaDeExpiracion, 
                estado, tipoDeUsuario, username, 
                 password):
        self.__idCredencial = idCredencial
        self.__fechaDeCreacion =fechaDeCreacion
        self.__fechaDeExpiracion =fechaDeExpiracion
        self.__estado =estado
        self.__tipoDeUsuario =tipoDeUsuario
        self.__username =username
        self.__password = password

        # Getter y Setter para idCredencial
    def get_idCredencial(self):
        return self.__idCredencial

    def set_idCredencial(self, idCredencial):
        self.__idCredencial = idCredencial

    # Getter y Setter para fechaDeCreacion
    def get_fechaDeCreacion(self):
        return self.__fechaDeCreacion

    def set_fechaDeCreacion(self, fechaDeCreacion):
        self.__fechaDeCreacion = fechaDeCreacion

    # Getter y Setter para fechaDeExpiracion
    def get_fechaDeExpiracion(self):
        return self.__fechaDeExpiracion

    def set_fechaDeExpiracion(self, fechaDeExpiracion):
        self.__fechaDeExpiracion = fechaDeExpiracion

    # Getter y Setter para estado
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    # Getter y Setter para tipoDeUsuario
    def get_tipoDeUsuario(self):
        return self.__tipoDeUsuario

    def set_tipoDeUsuario(self, tipoDeUsuario):
        self.__tipoDeUsuario = tipoDeUsuario

    # Getter y Setter para username
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    # Getter y Setter para password
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

