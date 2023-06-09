class Reporte:
    def __init__(self, descripcion, tipoDeReporte):
        self.__descripcion = descripcion
        self.__tipoDeReporte = tipoDeReporte

    # Getter y Setter para descripcion
    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    # Getter y Setter para tipoDeReporte
    def get_tipoDeReporte(self):
        return self.__tipoDeReporte

    def set_tipoDeReporte(self, tipoDeReporte):
        self.__tipoDeReporte = tipoDeReporte

    def generar_reporte_hospital(self, hospital):
        reporte = f"Reporte del Hospital: {1} \n"
        reporte += f"Nombre: {hospital.get_nombreDeHospital()}\n"
        reporte += f"Dirección: {hospital.get_direccion()}\n"
        reporte += f"Teléfono: {hospital.get_telefono()}\n"
        reporte += f"Estado: {hospital.get_estado()}\n"
        reporte += f"Condiciones: {', '.join(hospital.get_condiciones())}\n"
        reporte += f"Beneficios: {', '.join(hospital.get_beneficios())}\n"
        reporte += f"Horarios: {', '.join(hospital.get_horarios())}\n"
        return reporte

    def generar_reporte_donante(self, donante):
        reporte = f"Reporte del Donante: {1} \n"
        reporte += f"Nombre: {donante.get_nombre()}\n"
        reporte += f"Dirección: {donante.get_direccion()}\n"
        reporte += f"Teléfono: {donante.get_telefono()}\n"
        reporte += f"Tipo de Sangre: {donante.get_tipoSangre()}\n"
        reporte += f"Última Donación: {donante.get_ultimaDonacion()}\n"
        reporte += f"Registro de Donaciones: {donante.get_registroDonaciones()}\n"
        return reporte

    def generar_reporte_numero_hospitales(self, hospitales):
        total_hospitales = len(hospitales)
        reporte = f"Número de hospitales en el sistema: {total_hospitales}"
        return reporte

    def generar_reporte_numero_donantes(self, donantes):
        total_donantes = len(donantes)
        reporte = f"Número de donantes en el sistema: {total_donantes}"
        return reporte
