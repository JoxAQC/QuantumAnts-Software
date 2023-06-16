import os
import sqlite3 as sql

class OperacionCondicion:
    def _init_(self):
        pass

    def agregarCondicion(self,condicion):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()

        instruction = "INSERT INTO Condicion (idCondicion, descripcion, idHospital) VALUES (?, ?, ?)"
        cursor.execute(instruction, (condicion.get_idCondicion(), condicion.get_descripcion(), condicion.get_idHospital()))
        conn.commit()

        conn.close()
        return True  # La condición se agregó correctamente
    
    def eliminarCondicion(self,condicion):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()

        instruction = "DELETE FROM Condicion WHERE idCondicion = ?"
        cursor.execute(instruction, (condicion.get_idCondicion(),))
        conn.commit()

        conn.close()
        return True  # La condición se eliminó correctamente
