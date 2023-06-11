from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class Reporte:
    def __init__(self, descripcion, tipoDeReporte):
        self.__descripcion = descripcion
        self.__tipoDeReporte = tipoDeReporte

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

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

    def generar_informe_donacion(self, donaciones, formato='texto'):
        if formato == 'texto':
            return self._generar_informe_donacion_texto(donaciones)
        elif formato == 'pdf':
            return self._generar_informe_donacion_pdf(donaciones)
        else:
            raise ValueError("Formato no válido. Se admite 'texto' o 'pdf'.")

    def _generar_informe_donacion_texto(self, donaciones):
        reporte = "Informe de Donaciones\n"
        reporte += "----------------------\n"
        for donacion in donaciones:
            reporte += f"Fecha de Donación: {donacion.fecha}\n"
            reporte += f"Tipo de Sangre: {donacion.tipo_sangre}\n"
            reporte += f"Hospital: {donacion.hospital}\n"
            reporte += f"Cantidad de Sangre Donada: {donacion.cantidad}\n"
            reporte += "----------------------\n"
        return reporte

    def _generar_informe_donacion_pdf(self, donaciones):
        # Crear el documento PDF
        doc = SimpleDocTemplate("informe_donacion.pdf", pagesize=letter)

        # Definir el estilo del texto
        styles = getSampleStyleSheet()
        estilo_normal = styles['Normal']

        # Crear una lista para almacenar los elementos del informe
        elementos = []

        # Agregar el título
        titulo = Paragraph("Informe de Donaciones", estilo_normal)
        elementos.append(titulo)
        elementos.append(Spacer(1, 12))

        # Agregar los detalles de las donaciones
        for donacion in donaciones:
            fecha = Paragraph(f"<b>Fecha de Donación:</b> {donacion.fecha}", estilo_normal)
            tipo_sangre = Paragraph(f"<b>Tipo de Sangre:</b> {donacion.tipo_sangre}", estilo_normal)
            hospital = Paragraph(f"<b>Hospital:</b> {donacion.hospital}", estilo_normal)
            cantidad = Paragraph(f"<b>Cantidad de Sangre Donada:</b> {donacion.cantidad}", estilo_normal)

            elementos.append(fecha)
            elementos.append(tipo_sangre)
            elementos.append(hospital)
            elementos.append(cantidad)
            elementos.append(Spacer(1, 12))

        # Construir el documento PDF
        doc.build(elementos)

    def generar_informe_estadistico(self, estadisticas, formato='texto'):
        if formato == 'texto':
            return self._generar_informe_estadistico_texto(estadisticas)
        elif formato == 'pdf':
            return self._generar_informe_estadistico_pdf(estadisticas)
        else:
            raise ValueError("Formato no válido. Se admite 'texto' o 'pdf'.")

    def _generar_informe_estadistico_texto(self, estadisticas):
        reporte = "Informe Estadístico\n"
        reporte += "----------------------\n"
        reporte += f"Total de Donaciones: {estadisticas.total_donaciones}\n"
        reporte += f"Tipo de Sangre Más Donado: {estadisticas.tipo_sangre_mas_donado}\n"
        reporte += f"Hospitales con Más Donaciones: {1} \n"
        for hospital, cantidad in estadisticas.hospitales_mas_donaciones.items():
            reporte += f" - {hospital}: {cantidad} donaciones\n"
        reporte += "----------------------\n"
        return reporte

    def _generar_informe_estadistico_pdf(self, estadisticas):
        # Crear el documento PDF
        doc = SimpleDocTemplate("informe_estadistico.pdf", pagesize=letter)

        # Definir el estilo del texto
        styles = getSampleStyleSheet()
        estilo_normal = styles['Normal']

        # Crear una lista para almacenar los elementos del informe
        elementos = []

        # Agregar el título
        titulo = Paragraph("Informe Estadístico", estilo_normal)
        elementos.append(titulo)
        elementos.append(Spacer(1, 12))

        # Agregar las estadísticas
        total_donaciones = Paragraph(f"<b>Total de Donaciones:</b> {estadisticas.total_donaciones}", estilo_normal)
        tipo_sangre = Paragraph(f"<b>Tipo de Sangre Más Donado:</b> {estadisticas.tipo_sangre_mas_donado}", estilo_normal)
        hospitales = Paragraph("<b>Hospitales con Más Donaciones:</b>", estilo_normal)

        elementos.append(total_donaciones)
        elementos.append(tipo_sangre)
        elementos.append(hospitales)

        # Agregar los hospitales con más donaciones
        for hospital, cantidad in estadisticas.hospitales_mas_donaciones.items():
            texto_hospital = Paragraph(f"- {hospital}: {cantidad} donaciones", estilo_normal)
            elementos.append(texto_hospital)

        # Construir el documento PDF
        doc.build(elementos)
