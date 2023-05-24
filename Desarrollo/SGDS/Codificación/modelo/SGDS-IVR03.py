""""
from datetime import datetime, date, time

class Donante:
    def __init__(self, idDonante, nombre, fecha_nacimiento, docIdentidad, telefono, direccion, grupo_sanguineo, RH):
        self.idDonante = idDonante
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.docIdentidad = docIdentidad
        self.telefono = telefono
        self.direccion = direccion
        self.grupo_sanguineo = grupo_sanguineo
        self.RH = RH
        self.ultimaDonacion = None

class Hospital:
    def __init__(self, nombreDeHospital, direccion, telefono, estado, horario):
        self.nombreDeHospital = nombreDeHospital
        self.direccion = direccion
        self.telefono = telefono
        self.estado = estado
        self.horario = horario

    def programarCita(self, donante, fecha):
        hora_cita = self.horario.hora_inicio
        fecha_cita = datetime.combine(fecha, hora_cita)  # Combina la fecha con la hora de inicio del horario

        # Verifica que la fecha de la cita sea posterior o igual a la fecha actual y que la hora esté dentro del horario de atención
        if fecha_cita.date() >= date.today() and hora_cita <= self.horario.hora_fin:
            cita = Cita(len(Cita.citas) + 1, fecha_cita, donante, self)
            Cita.citas.append(cita)
            donante.ultimaDonacion = fecha_cita.date()
            return True
        else:
            print("El hospital no puede programar una cita en la fecha especificada.")
            return False

class HorarioDeAtencion:
    def __init__(self, descripcion, hora_inicio, hora_fin):
        self.descripcion = descripcion
        self.hora_inicio = datetime.strptime(hora_inicio, "%I:%M %p").time()  # Convierte la cadena de hora_inicio a tipo time
        self.hora_fin = datetime.strptime(hora_fin, "%I:%M %p").time()  # Convierte la cadena de hora_fin a tipo time

class Cita:
    citas = []

    def __init__(self, idCita, fecha, donante, hospital):
        self.idCita = idCita
        self.fecha = fecha
        self.donante = donante
        self.hospital = hospital
        self.estado = False

    def confirmarCita(self):
        print("Detalles de la cita:")
        print("Donante:", self.donante.nombre)
        print("Hospital:", self.hospital.nombreDeHospital)
        print("Fecha:", self.fecha)
        confirmacion = input("¿Desea confirmar esta cita? (s/n): ")
        if confirmacion.lower() == "s":
            self.estado = True
            return True
        else:
            return False

    def finalizarCita(self):
        # Verifica si la fecha de la cita es anterior a la fecha actual para poder finalizarla
        if self.fecha.date() < date.today():
            self.donante.ultimaDonacion = self.fecha.date()
            Cita.citas.remove(self)
            return True
        else:
            return False

    def reprogramarCita(self, fechaNueva):
        self.fecha = datetime.combine(fechaNueva, self.fecha.time())  # Combina la nueva fecha con la hora existente
        self.hospital.programarCita(self.donante, fechaNueva)
        Cita.citas.remove(self)
        return True


# Ejemplo de uso
horario_atencion = HorarioDeAtencion("Horario de atención", "9:00 AM", "5:00 PM")

hospital = Hospital("Hospital General", "Calle Principal", "123456789", True, horario_atencion)

donante = Donante(1, "Juan Pérez", date(1985, 5, 10), "1234567890", "987654321", "Calle 123", "A+", "RH+")

fecha_cita = date(2023, 6, 10)  # Fecha de la cita

hospital.programarCita(donante, fecha_cita)

print("Citas programadas:")
for cita in Cita.citas:
    print(cita.idCita, cita.fecha, cita.donante.nombre, cita.hospital.nombreDeHospital)

# Confirmar cita
#if Cita.citas:
  #  cita = Cita.citas[0]
 #   cita.confirmarCita()
#else:
   # print("No hay citas programadas.")

# Finalizar cita (simulación)
if Cita.citas:
    cita = Cita.citas[0]
    cita.finalizarCita()

#Reprogramar cita
if Cita.citas:
    cita = Cita.citas[0]
    cita.reprogramarCita(date(2023, 7, 15))
"""