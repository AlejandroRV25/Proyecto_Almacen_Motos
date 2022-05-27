
class Servicio:
    def __init__(self, precio, fecha, tipo, problema):
        self.precio = precio
        self.fecha = fecha
        self.tipo = tipo
        self.problema = problema

    def servicio(self):
        pass

    def get_precio(self):
        return self.precio

    def get_fecha(self):
        return self.fecha

    def get_tipo(self):
        return self.tipo

    def get_problema(self):
        return self.problema

    def set_precio(self, precio):
        self.precio = precio

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_problema(self, problema):
        self.problema = problema

    def Registro_Servicio(servicio,csv,string,os):
        cantidad = int(input('tipo de servicio'))
        
        with open(servicio, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                PrecioServ = int('rh: ')
                FechaServ = string('ventas realizadas: ')
                tipo = string(' tipo de servicio: ')
                problema = string('tipo de problema: ')
                writer.writerow([ PrecioServ, FechaServ, tipo, problema])
                
    def Recuperar_Servicio(servicio,os,cvs):
        os.system('cls')
        print('el servicio sera:')
        with open(servicio, 'r', newline='') as archivo_csv:
            reader = cvs.reader(archivo_csv)
            for linea in reader:
                print(f'PrecioServ: {linea[0]}')
                print(f'FechaServ: {linea[1]}')
                print(f'tipo: {linea[2]}')
                print(f'problema: {linea[3]}')    
