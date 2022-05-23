import os
import csv
class Factura:
    def __init__(self, producto:producto, cliente:cliente, fecha:string, numFactura:int):
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
    def Factura(factura):
        cantidad = int(input('facturas a registrar'))
        
        with open(factura, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                cliente = cliente ('cliente: ')
                fecha = fecha ('fecha: ')
                numFactura = numFactura ('numero de factura: ')
                producto = producto ('producto: ')
       
                
                
            
            
