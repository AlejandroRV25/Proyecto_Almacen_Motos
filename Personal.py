from Usuario import Usuario
from DatoContacto import DatoContacto
from Sede import Sede
class Personal:
    def __init__(self, rh, ventas):
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

    def Registro_Personal(personal,csv,os,string):
        cantidad = int(input('informacion del cliente'))
        
        with open(personal, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                rh = string('rh: ')
                ventas = int('ventas realizadas: ')
                writer.writerow([ rh, ventas])
                
    def Recuperar_personal(personal,os,cliente,cvs):
        os.system('cls')
        print('datos del personal:')
        with open(personal, 'r', newline='') as archivo_csv:
            reader = cvs.reader(archivo_csv)
            for linea in reader:
                print(f'rh: {linea[0]}')
                print(f'ventas: {linea[1]}')    
            
