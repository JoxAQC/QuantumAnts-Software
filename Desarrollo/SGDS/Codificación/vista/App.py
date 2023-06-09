from modelo.Hospital import Hospital
from modelo.Donante import Donante
from modelo.OperacionDonante import OperacionDonante
from modelo.OperacionHospital import OperacionesHospital
from modelo.OperacionBeneficio import OperacionBeneficio
from modelo.OperacionCredencial import OperacionCredencial
from modelo.Credencial import Credencial
from modelo.Horario import Horario
from modelo.Beneficio import Beneficio
from modelo.Reporte import Reporte

# Agregar beneficios
oper_beneficio = OperacionBeneficio()
beneficio1 = Beneficio(1, "Chequeo general", 1, "18L", "7")
beneficio2 = Beneficio(2, "Tomografia", 1, "16L", "0")
beneficios = list()

beneficios.append(beneficio1)
beneficios.append(beneficio2)

credencial1 = Credencial(1, "12-12-12", "12-12-17", "Activo", "Donante","el miau", "lamala")
credencial2 = Credencial(2, "12-12-12", "12-12-17", "Activo", "Donante","el perro", "messimalo")
credencial3 = Credencial(3, "12-12-12", "12-12-17", "Activo", "Donante","loayza", "loayza")

# Agregar Credenciales
oper_credencial = OperacionCredencial()
oper_credencial.registrar_credencial(credencial1)
oper_credencial.registrar_credencial(credencial2)
oper_credencial.registrar_credencial(credencial3)

persona1 = Donante(1, "Remi", "12-12-12", "7654321", "98765433", "Los Perales", beneficio1, "o+", "rh+", "nulo", "1")
persona2 = Donante(2, "Raul", "12-15-12", "7674321", "98765444", "Los Jiros", beneficio2, "o-", "rh-", "nulo", "2")

horario = Horario(1, "Lunes-Martes-Miercoles", "9am-9pm", 1)

hospital1 = Hospital(1, "Loayza", "Garzas", "654-321", "Activo", "nulo", "no hay", horario, credencial3)

oper_beneficio.agregar_grupo_beneficios(hospital1, beneficios)

oper_donante = OperacionDonante()
oper_hospital = OperacionesHospital(1)

# Registrar donantes
oper_donante.registrar_donante(persona1)
oper_donante.registrar_donante(persona2)

# Agregar hospital a la base de datos
oper_hospital.agregar_hospital_bd(hospital1)

# Obtener beneficios obtenidos por un donante
oper_beneficio.ver_beneficios_obtenidos(persona1)

# Generar reporte del hospital
reporte_hospital = Reporte("Reporte del Hospital", "Hospital")
print(reporte_hospital.generar_reporte_hospital(hospital1))

# Generar reporte del donante
reporte_donante = Reporte("Reporte del Donante", "Donante")
print(reporte_donante.generar_reporte_donante(persona1))

# Generar reporte de número de hospitales en el sistema
hospitales = [hospital1]
reporte_numero_hospitales = Reporte("Reporte de Número de Hospitales", "Número de Hospitales")
print(reporte_numero_hospitales.generar_reporte_numero_hospitales(hospitales))

# Generar reporte de úmero de donantes en el sistema
donantes = [persona1, persona2]
reporte_numero_donantes = Reporte("Reporte  de Número de Donantes", "Número de Donantes")
print(reporte_numero_donantes.generar_reporte_numero_donantes(donantes))
