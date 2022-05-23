import os
import csv
class RegistroDeVentas:
    def __init__(self, servicio:servicio, factura:factura, RegistroVentas:RegistroVentas):
        self.servicio = servicio
        self.factura = factura
        self.registro = registro

    def registro_ventas(self):
        pass
    
    def RegistroDeVentas(registro):
        cantidad = int(input('registro de ventas'))
        
        with open(registro, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                servicio = servicio ('servicio: ')
                factura = factura ('factura: ')
                RegistroVentas = RegistroVentas ('Registro de Ventas: ')
                
    
