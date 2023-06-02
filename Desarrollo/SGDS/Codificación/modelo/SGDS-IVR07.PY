class Reporte:
    def __init__(self, descripcion, tipoDeReporte):
        self.__descripcion = descripcion
        self.__tipoDeReporte = tipoDeReporte
        
    # Getter y Setter para  descripcion
    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
        
    # Getter y Setter para  tipoDeReporte
    def get_tipoDeReporte(self):
        return self.__tipoDeReporte

    def set_tipoDeReporte(self, tipoDeReporte):
        self.__tipoDeReporte = tipoDeReporte  