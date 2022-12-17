from tabulate import tabulate
import pymysql
import os


class Efectividad:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='Pelusa24#',
            db='fidelizacion2'
        )

        self.cursor = self.conn.cursor()
        self.Efectividad = ""
        self.nuevo_efectividad = ""


    def Submenu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Bienvenido a la tabla Efectividad")
            print("1. Insertar")
            print("2. Mostrar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menu de tablas")
            try:
                opc = int(input("Indique la opcion deseada: \n"))
                if(opc == 1 ):
                    self.Insertar()
                elif(opc == 2):
                    self.Mostrar()
                elif(opc == 3):
                    self.Actualizar()
                elif(opc == 4):
                    self.Eliminar()
                elif(opc == 5):
                    Salida = False
                else:
                    print("Opcion no diponible")
                    os.system("pause")
            except ValueError:
                print("Debe ingresar un numero")
                os.system("pause")

    def Insertar(self):
        os.system("cls")
        self.Efectividad = input("Ingrese la efectividad de la comunicacion: \n")
        if not self.Efectividad:
            print("El campo no puede estar vacio")
        else:
            sql = "insert into efectividad(Efectividad) values('{}')".format(self.Efectividad)
            self.cursor.execute(sql)
            print("Ingresado correctamente")
            self.conn.commit()
        os.system('pause')

    def Mostrar(self):
        os.system("cls")
        sql = "select * from efectividad"
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id" , "Efectividad"]
        for row in rows:
            print(tabulate(row, headers = headers))
        os.system('pause')

    def Actualizar(self):
        os.system("cls")
        self.Efectividad = input("Indique la efectividad de la comunicacion a modificar: \n")
        self.nuevo_efectividad = input("Indique la nueva efectividad de la comunicacion:  \n")
        if len(self.Efectividad) == 0 or len(self.nuevo_efectividad) == 0:
            print("Uno de los campos no puede estar vacio")
        else:
            sql = "update efectividad set Efectividad = '{}' where Efectividad = '{}'".format(self.nuevo_efectividad, self.Efectividad)
            self.cursor.execute(sql)
            print("Elemento actualizado")
            self.conn.commit()
        os.system('pause')

    def Eliminar(self):
        os.system("cls")
        self.Efectividad = input("Indique el tipo de comunicacion a eliminar: \n ")
        if not self.Efectividad:
            print("El campo no puede estar vacio")
        else:
            sql = "delete from efectividad where Efectividad = '{}'".format(self.Efectividad)
            self.cursor.execute(sql)
            print("Elemento eleminado")
            self.conn.commit()
        os.system('pause')
