from tabulate import tabulate
import pymysql
import os



class Mensajes:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='Pelusa24#',
            db='fidelizacion2'
        )

        self.cursor = self.conn.cursor()
        self.Mensaje = ""
        self.nuevo_Mensaje = ""

    def Submenu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Bienvenido a la tabla Mensajes")
            print("1. Insertar")
            print("2. Mostrar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menu de tablas")
            try:
                opc = int(input("Indique la opcion deseada:\n"))
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
        self.Mensaje = input("Ingrese el tipo de mensaje:\n")
        if not self.Mensaje:
            print("El campo no puede estar vacio")
        else:
            sql = "insert into mensajes(Mensaje) values('{}')".format(self.Mensaje)
            self.cursor.execute(sql)
            print("Ingresado correctamente")
            self.conn.commit()
        os.system('pause')

    def Mostrar(self):
        os.system("cls")
        sql = "select * from mensajes"
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id" , "Mensaje"]
        for row in rows:
            print(tabulate(row, headers = headers))
        os.system('pause')

    def Actualizar(self):
        os.system("cls")
        self.Mensaje = input("Indique el tipo de mensaje modificar:\n")
        self.nuevo_Mensaje = input("Indique el nuevo tipo de mensaje:\n")
        if len(self.Mensaje) == 0 or len(self.nuevo_Mensaje) == 0:
            print("Uno de los campos no puede estar vacio")
        else:
            sql = "update mensajes set Mensaje = '{}' where Mensaje = '{}'".format(self.nuevo_Mensaje, self.Mensaje)
            self.cursor.execute(sql)
            print("Elemento actualizado")
            self.conn.commit()
        os.system('pause')

    def Eliminar(self):
        os.system("cls")
        self.Mensaje = input("Indique el tipo de mensaje a eliminar:\n ")
        if not self.Mensaje:
            print("El campo no puede estar vacio")
        else:
            sql = "delete from mensajes where Mensaje = '{}'".format(self.Mensaje)
            self.cursor.execute(sql)
            print("Elemento eleminado")
            self.conn.commit()
        os.system('pause')

