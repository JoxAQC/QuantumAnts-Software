class HorarioDeAtencion:
    def __init__(self, descripcion, hora):
        self.descripcion = descripcion
        self.hora = hora

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_hora(self):
        return self.hora

    def set_hora(self, hora):
        self.hora = hora
