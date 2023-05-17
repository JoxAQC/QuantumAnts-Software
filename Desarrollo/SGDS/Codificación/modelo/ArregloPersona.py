from Persona import Persona

class ArregloPersona:
    def __init__(self):
        self.__arreglo = []

    def agregar_persona(self, persona):
        self.__arreglo.append(persona)

    def eliminar_persona(self, nombre):
        for persona in self.__arreglo:
            if persona.get_nombre() == nombre:
                self.__arreglo.remove(persona)
                return True
        return False

    def buscar_persona(self, nombre):
        for persona in self.__arreglo:
            if persona.get_nombre() == nombre:
                return persona
        return None

