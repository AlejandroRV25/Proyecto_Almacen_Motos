import os
import csv
class Factura:
    def __init__(self, producto:producto, cliente:cliente):
        self.producto = producto
        self.cliente = cliente


    def factura(self):
        pass

    def get_numFactura(self):
        return self.numFactura

    def set_numFactura(self, numFactura):
        self.numFactura = numFactura
    def Factura(factura):
        cantidad = int(input('facturas a registrar'))
        
        with open(factura, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                cliente = cliente ('cliente: ')
                fecha = string ('fecha: ')
                numFactura = int ('numero de factura: ')
                producto = producto ('producto: ')
                writer.writerow([cliente, fecha, numFactura, producto])
       
                
                
            
            
