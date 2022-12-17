from Personas import Personas
from Comunicacion import Comunicacion
from Efectividad import Efectividad
from Roles import Roles
from Mensaje import Mensajes
from Fidelizacion import Fidelizacion
import os


class Menu:
    def __init__(self):
        self.Comunicacion = Comunicacion()
        self.Roles = Roles()
        self.Personas = Personas()
        self.Efectividad = Efectividad()
        self.Mensaje = Mensajes()
        self.Fide = Fidelizacion()

    def Menu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Bienvenido a la aplicación de fidelización")
            print("indique una de las siguientes opciones")
            print(" 1. Acceder a la base de datos:")
            print(" 2. Clientes fidelizados")
            print(" 3. Salir")
            try:
                opc = int(input("Indique la opcion deseada \n"))
                if(opc == 1 ):
                    self.BaseDeDatos()
                elif(opc == 2):
                    self.Fidelizacion()
                elif(opc == 3):
                    Salida = False
                else:
                    print("Opcion no diponible")
                    os.system("pause")
            except ValueError:
                print("Debe ingresar un numero")
                os.system("pause")



    def BaseDeDatos(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Seleccione una tabla:")
            print("1. Personas")
            print("2. Roles")
            print("3. Tipo De Comunicacion")
            print("4. Efectividad de la Comunicacion")
            print("5. Tipo de Mensaje")
            print("6. Salir al menu principal")
            try:
                opc = int(input("Indique la opcion deseada \n"))
                if(opc == 1 ):
                    self.Personas.Submenu()
                elif(opc == 2):
                    self.Roles.Submenu()
                elif(opc == 3):
                    self.Comunicacion.Submenu()
                elif(opc == 4):
                    self.Efectividad.Submenu()
                elif(opc == 5):
                    self.Mensaje.Submenu()
                elif(opc == 6):
                    Salida = False
                else:
                    print("Opcion no diponible")
                    os.system("pause")
            except ValueError:
                    print("Debe ingresar un numero")
                    os.system("pause")



    def Fidelizacion(self):
        self.Fide.Submenu()


if __name__ == '__main__':
    P = Menu()
    P.Menu()

