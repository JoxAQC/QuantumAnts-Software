from datetime import datetime

class Cita:
    def __init__(self, idCita, fecha, donante, hospital, estado):
        self.idCita = idCita
        self.fecha = fecha
        self.donante = donante
        self.hospital = hospital
        self.estado = estado
    
    # Métodos setter y getter para la variable idCita
    def set_idCita(self, idCita):
        self.idCita = idCita
        
    def get_idCita(self):
        return self.idCita
    
    # Métodos setter y getter para la variable fecha
    def set_fecha(self, fecha):
        self.fecha = fecha
        
    def get_fecha(self):
        return self.fecha
    
    # Métodos setter y getter para la variable donante
    def set_donante(self, donante):
        self.donante = donante
        
    def get_donante(self):
        return self.donante
    
    # Métodos setter y getter para la variable hospital
    def set_hospital(self, hospital):
        self.hospital = hospital
        
    def get_hospital(self):
        return self.hospital
    
    # Métodos setter y getter para la variable estado
    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
