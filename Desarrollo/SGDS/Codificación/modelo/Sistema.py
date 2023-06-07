import sqlite3 as sql
import os

class Sistema:
    def __init__(self, estado):
        self.__estado = estado
    
    # Base de datos
    @staticmethod
    def conectar_bd():  
        # Obtener la ruta absoluta al archivo de base de datos
        current_directory = os.path.abspath("")
        db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

        # Establecer conexión con la base de datos
        conn = sql.connect(db_path)
        return conn

    # Getter y Setter para estado
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado
