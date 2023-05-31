from datetime import datetime

class Cita:
    def __init__(self, idCita, fecha, donante, hospital, estado):
        self.__idCita = idCita
        self.__fecha = fecha
        self.__donante = donante
        self.__hospital = hospital
        self.__estado = estado
    
    # Métodos setter y getter para la variable idCita
    def set_idCita(self, idCita):
        self.__idCita = idCita
        
    def get_idCita(self):
        return self.__idCita
    
    # Métodos setter y getter para la variable fecha
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def get_fecha(self):
        return self.__fecha
    
    # Métodos setter y getter para la variable donante
    def set_donante(self, donante):
        self.__donante = donante
        
    def get_donante(self):
        return self.__donante
    
    # Métodos setter y getter para la variable hospital
    def set_hospital(self, hospital):
        self.__hospital = hospital
        
    def get_hospital(self):
        return self.__hospital
    
    # Métodos setter y getter para la variable estado
    def set_estado(self, estado):
        self.__estado = estado
        
    def get_estado(self):
        return self.__estado
