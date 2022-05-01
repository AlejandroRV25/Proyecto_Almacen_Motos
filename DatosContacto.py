
class DatosContacto:
    def __init__(self, correo, telefono):
        self.correo = correo
        self.telefono = telefono

    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono
                