
class Servicio:
    def __init__(self, PrecioServ:int, FechaServ:string, tipo:string, problema:string):
        self.precio = precio
        self.fecha = fecha
        self.tipo = tipo
        self.problema = problema

    def servicio(self):
        pass

    def get_precio(self):
        return self.precio

    def get_fecha(self):
        return self.fecha

    def get_tipo(self):
        return self.tipo

    def get_problema(self):
        return self.problema

    def set_precio(self, precio):
        self.precio = precio

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_problema(self, problema):
        self.problema = problema
