#from modelo.Persona import Persona
from modelo.ArregloPersona import ArregloPersona, Persona

# Crear instancia de ArregloPersona
arreglo_persona = ArregloPersona()

# Agregar personas
persona1 = Persona("Juan", 20, "2003-05-01", "Pizza")
persona2 = Persona("María", 22, "2001-10-15", "Hamburguesa")
persona3 = Persona("Carlos", 19, "2004-02-28", "Sushi")

arreglo_persona.agregar_persona(persona1)
arreglo_persona.agregar_persona(persona2)
arreglo_persona.agregar_persona(persona3)

# Mostrar personas
print("Personas:")
for persona in arreglo_persona.get_personas():
    print(f"Nombre: {persona.get_nombre()}")
    print(f"Edad: {persona.get_edad()}")
    print(f"Fecha de nacimiento: {persona.get_fecha_nacimiento()}")
    print(f"Comida favorita: {persona.get_comida_favorita()}")
    print("-" * 10)
