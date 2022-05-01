
class Personal:
    def __init__(self, nombre, datoContacto, rh, documento, ventas):
        self.nombre = nombre
        self.datoContacto = datoContacto
        self.rh = rh
        self.documento = documento
        self.ventas = ventas

    def get_nombre(self):
        return self.nombre

    def get_rh(self):
        return self.rh

    def get_documento(self):
        return self.documento

    def get_ventas(self):
        return self.ventas

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_rh(self, rh):
        self.rh = rh

    def set_documento(self, documento):
        self.documento = documento

    def set_ventas(self, ventas):
        self.ventas = ventas
            