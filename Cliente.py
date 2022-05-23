
class Cliente:
    def __init__(self, Usuario:Usuario, datoContacto:DatoContacto):
        self.Usuario = Usuario
        self.DatoContacto = DatoContacto

    def cliente(self):
        pass

    def get_Usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.Usuario=usuario
