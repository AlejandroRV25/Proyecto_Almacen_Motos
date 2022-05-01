
class Cliente:
    def __init__(self, nomClien, datoContacto):
        self.nomClien = nomClien
        self.datoContacto = datoContacto

    def cliente(self):
        pass

    def get_nombre(self):
        return self.nomClien

    def set_nombre(self, nombre):
        self.nomClien = nombre
