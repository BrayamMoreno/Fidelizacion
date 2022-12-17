from tabulate import tabulate
import os
import pymysql
class Roles():
###################################################

    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='Pelusa24#',
            db='fidelizacion2'
        )
        self.cursor = self.conn.cursor()
        self.Rol = ""
        self.Nuevo_rol = ""




    def Submenu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Bienvenido a la tabla Roles")
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
        self.Rol = input("Ingrese un rol:\n")
        if not self.Rol:
            print("El campo no puede estar vacio")
        else:
            sql = "insert into roles(Rol) values('{}')".format(self.Rol)
            self.cursor.execute(sql)
            print("Ingresado correctamente")
            self.conn.commit()
        os.system("pause")

    def Mostrar(self):
        os.system("cls")
        sql = "select * from roles"
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id" , "Rol"]
        for row in rows:
            print(tabulate(row, headers = headers))
        os.system('pause')

    def Actualizar(self):
        os.system("cls")
        self.Rol = input("Indique el rol a modificar:\n")
        self.Nuevo_rol = input("Indique el nuevo rol:\n")
        if len(self.Rol) == 0 or len(self.Nuevo_rol) == 0 :
            print("Uno de los campos no puede estar vacio")
        else:
            sql = "update roles set rol = '{}' where rol = '{}'".format(self.Nuevo_rol, self.Rol)
            self.cursor.execute(sql)
            print("Elemento actualizado")
            self.conn.commit()
        os.system('pause')

    def Eliminar(self):
        os.system("cls")
        self.Rol = input("Indique el rol a eliminar:\n ")
        if not self.Rol:
            print("El campo no puede estar vacio")
        else:
            sql = "delete from roles where rol = '{}'".format(self.Rol)
            self.cursor.execute(sql)
            print("Elemento eleminado")
            self.conn.commit()
        os.system('pause')