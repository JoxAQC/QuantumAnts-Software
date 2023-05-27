import sqlite3 as sql
from Donante import Donante
from Sistema import Sistema

# Crear un objeto Donante
donante = Donante("123", "Juan Pérez", "1990-01-01", "12345678", "987654321", "Calle Principal 123", True, "A+", "+", "2023-05-20", "H001")

# Crear un objeto Sistema
sistema = Sistema()

# Registrar el donante en la base de datos utilizando el método de la clase Sistema
sistema.registrar_donante(donante)


