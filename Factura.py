
class Factura:
    def __init__(self, producto, cliente, fecha, numFactura):
        self.producto = producto
        self.cliente = cliente
        self.fecha = fecha
        self.numFactura = numFactura

    def factura(self):
        pass

    def get_fecha(self):
        return self.fecha

    def get_numFactura(self):
        return self.numFactura

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_numFactura(self, numFactura):
        self.numFactura = numFactura
            