from SGDS_IVR01 import Hospital
from Credenciales import Credencial
from Condiciones import Condiciones
from Beneficios import Beneficios
from Horarios import Horarios
from Cita import Cita
from HorarioDeAtencion import HorarioDeAtencion
import sqlite3 as sql
import os
import json
import random
from datetime import datetime, timedelta


class Donante:
    def __init__(self, nombre, edad, grupo_sanguineo, numero_identificacion):
        self.nombre = nombre
        self.edad = edad
        self.grupo_sanguineo = grupo_sanguineo
        self.numero_identificacion = numero_identificacion
        self.cuenta_registrada = False

    def registrar_cuenta(self):
        # Simulación del proceso de registro de cuenta
        self.cuenta_registrada = True
        print("Cuenta registrada con éxito.")

    def programar_cita(self, fecha, hora):
        # Simulación de la programación de una cita
        print(f"Se ha programado una cita para el {fecha} a las {hora}.")

    def ver_historial_donaciones(self):
        # Simulación de la visualización del historial de donaciones
        print("Historial de donaciones:")
        # Aquí se mostraría el historial real

    def ver_beneficios(self):
        # Simulación de la visualización de los beneficios
        print("Beneficios recibidos:")
        # Aquí se mostrarían los beneficios reales


class Hospital:
    def validar_cuenta(self, credenciales):
        # Simulación de la validación de cuenta
        if credenciales == "credenciales_validas":
            print("Cuenta validada con éxito.")
        else:
            print("Credenciales inválidas. Acceso denegado.")

    def validar_donacion(self, donante):
        # Simulación de la validación de donación
        if donante.edad >= 18:
            print("Donación validada. Se otorgará un beneficio al donante.")
        else:
            print("Donante no cumple con los requisitos para obtener el beneficio.")

    def ver_historial_donaciones(self):
        # Simulación de la visualización del historial de donaciones
        print("Historial de donaciones:")
        # Aquí se mostraría el historial real

    def ver_beneficios_otorgados(self):
        # Simulación de la visualización de los beneficios otorgados
        print("Beneficios otorgados:")
        # Aquí se mostrarían los beneficios reales


# Ejemplo de uso del sistema
donante = Donante("Juan Pérez", 25, "A+", "1234567890")
hospital = Hospital()

# Paso 1: Acceder al sistema
# No es necesario simular este paso, ya que asumimos que el donante y el hospital están accediendo al sistema de manera adecuada.

# Paso 2: Comprobar las precondiciones
if isinstance(donante, Donante):
    if not donante.cuenta_registrada:
        donante.registrar_cuenta()
    donante.programar_cita("2023-06-03", "10:00")

# Paso 3: Registrar o validar la cuenta (en el caso del hospital)
hospital.validar_cuenta("credenciales_validas")

# Paso 4: Programar una cita (donante)
donante.programar_cita("2023-06-03", "10:00")

# Paso 5: Validar la donación (hospital)
hospital.validar_donacion(donante)

# Paso 6: Ver el historial de donaciones y beneficios
donante.ver_historial_donaciones()
donante.ver_beneficios()
hospital.ver_historial_donaciones()
hospital.ver_beneficios_otorgados()
