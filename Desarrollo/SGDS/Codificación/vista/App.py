from modelo.Hospital import Hospital
from modelo.Donante import Donante
from modelo.Credencial import Credencial
<<<<<<< HEAD
from modelo.Registro import Registro

registrar = Registro(True)
donante = Donante(1, "Juan Pérez", "date(1985, 5, 10)", "1234567890", "987654321", "Calle 123", "A+", "RH+")
credencial = Credencial(1, "12/02/2024","12/02/2025", "Activo", "Donante", 
                        "RogelioElCrag", "1234")
registrar.insertar_credencial(credencial)
hospital = Hospital("Maria Auxiliadora", "Las Perlas #524", "987654321", 
                    "Activo", "No Creado", "No Creado", "No creado", credencial)
registrar.agregarHospitalBD(hospital)
=======
from modelo.Condiciones import Condiciones
from modelo.Beneficios import Beneficios
from modelo.Horarios import Horarios
import sqlite3 as sql
import os
import json

print("hola")
#credencial = Credencial(1, "12/02/2024","12/02/2025", "Activo", "Donante", 
#                       "RogelioElCrag", "1234")
>>>>>>> 66e0230f2f20bdfa0636dced2301eaa2ce498085
