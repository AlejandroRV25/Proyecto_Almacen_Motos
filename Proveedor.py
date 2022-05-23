
class Proveedor:
    def __init__(self, NombProv:string, direccion:string, DatosContacto:DatoContacto):
        self.nombProv = NombProv
        self.direccion = direccion
        self.datosContacto = DatosContacto

    def proveedor(self):
        pass

    def get_nombre(self):
        return self.nombProv

    def get_direccion(self):
        return self.direccion

    def set_nombre(self, nombre):
        self.nombProv = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion
        
