import os
import csv
class DatoContacto:
    def __init__(self, correo:string, telefono:int):
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
        
    def Registro_Dato_Contacto(contacto):
        cantidad = int(input('informacion a recibir'))
        
        with open(contacto, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                correo = input('correo: ')
                telefono = input('telefono: ')
                writer.writerow([ telefono, correo])
                
    def Registro_Dato_Contacto(contacto):
        os.system('cls')
        print('contactos registrados:')
        with open(contacto, 'r', newline='') as archivo_csv:
            reader = cvs.reader(archivo_csv)
            for linea in reader:
                print(f'telefono: {linea[0]}')
                print(f'correo: {linea[1]}')
            
                
