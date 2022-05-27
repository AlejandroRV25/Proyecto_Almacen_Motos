from Usuario import Usuario
from DatoContacto import DatoContacto 
import os
import csv
class Cliente:
    def __init__(self, Usuario):
        self.Usuario = Usuario
    def Registro_Cliente(cliente):
        cantidad = int(input('informacion del cliente'))
        
        with open(cliente, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                Usuario = Usuario('usuario: ')
                DatoContacto = DatoContacto('datos del contacto: ')
                writer.writerow([ Usuario, DatoContacto])
                
    def Recuperar_Cliente(cliente,cvs):
        os.system('cls')
        print('datos del cliente:')
        with open(cliente, 'r', newline='') as archivo_csv:
            reader = cvs.reader(archivo_csv)
            for linea in reader:
                print(f'datos del cliente: {linea[0]}')
