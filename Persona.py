
class Personal:
    def __init__(self, rh:string, ventas:int):
        self.rh = rh
        self.ventas = ventas

    def get_rh(self):
        return self.rh

    def get_ventas(self):
        return self.ventas

    def set_rh(self, rh):
        self.rh = rh

    def set_ventas(self, ventas):
        self.ventas = ventas
            
