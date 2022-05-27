
class Usuario:
    def __init__(self, nombre:string, documento:int, datoContacto:datoContacto):
        self.nombre = nombre
        self.documento = documento
        self.datosContacto = datoContacto

    def get_nombre(self):
        return self.nombre

    def get_documento(self):
        return self.documento

    def set_nombre(self, nombre):
        self.nombProv = nombre

    def set_direccion(self, documento):
        self.documento = documento
        
