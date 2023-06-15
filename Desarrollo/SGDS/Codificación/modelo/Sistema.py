import sqlite3 as sql
import os

class Sistema:
    def __init__(self, estado):
        self.__estado = estado
    
    # Base de datos
    @staticmethod
    def conectar_bd():  
        # Establecer conexión con la base de datos
        conn = sql.connect("SGDS-VABD01.db")
        return conn

    # Getter y Setter para estado
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado
