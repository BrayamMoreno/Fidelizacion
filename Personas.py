from tabulate import tabulate
import pymysql
import os
############################################################
class Personas:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='Pelusa24#',
            db='fidelizacion2'
        )

        self.cursor = self.conn.cursor()
        self.Nombres = ""
        self.Apellidos = ""
        self.Cedula = 0
        self.Celular = 0
        self.Email = 0
        self.Sexo = 0
        self.Rol = 0
        self.Comunicacion = 0
        self.Efectividad = 0
        self.Mensaje = 0
        self.Id = 0

    def Submenu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Bienvenido a la tabla Personas")
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
        try:
            self.Nombres = input("Ingrese los nombres:\n")
            self.Apellidos = input("Ingrese los apellidos:\n")
            self.Email = input("Indique el correo:\n")
            self.Sexo =input("Indique su sexo:\n")
            self.Cedula = int(input("Indique la cedula: \n"))
            self.Celular = int(input("Indique su numero de celular: \n"))
            self.Rol =int(input("Indique el Id del rol que cumple: \n"))
            self.Comunicacion = int(input("Indique el Id de la comunicacion que se realizo: \n"))
            self.Efectividad = int(input("Indique el Id de la efectividad de la comunicacion: \n"))
            self.Mensaje = int(input("Indique el id de el mensaje enviado: \n"))
        except ValueError:
            print("Deben ingresarse numeros o usted tiene espacios en blanco ")
        else:
            sql = "insert into personas(Nombres,Apellidos,Cedula,Celular,Email,Sexo,IdRol,IdComunicacion,IdEfectividad,IdMensaje) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.Nombres,self.Apellidos,self.Cedula,self.Celular,self.Email,self.Sexo,self.Rol,self.Comunicacion,self.Efectividad,self.Mensaje)
            self.cursor.execute(sql)
            print("Ingresado correctamente")
            self.conn.commit()
        os.system('pause')

    def Eliminar(self):
        os.system("cls")
        try:
            self.Cedula = int(input("Indique la cedula del registro a eliminar: \n"))
        except ValueError:
            print("Debe ingresarse un numero")
        if not self.Cedula:
            print("El campos no puede estar vacio")
        else:
            sql = "delete from personas where Cedula = '{}'".format(self.Cedula)
            self.cursor.execute(sql)
            print("Elemento eleminado")
            self.conn.commit()
        os.system('pause')

    def Mostrar(self):
        os.system("cls")
        sql = "select * from personas"
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id","Nombre","Apellidos","Cedula","Celular","Email","Sexo","Rol","Comunicacion","Efectividad","Mensaje"]
        for row in rows:
           print(tabulate(row, headers = headers))
        os.system('pause')

    def Actualizar(self):
        os.system("cls")
        try:
            self.Id  = int(input("Indique el Id del registro modificar:\n"))
            self.Nombres = input("Ingrese los nombres:\n")
            self.Apellidos = input("Ingrese los apellidos:\n")
            self.Email = input("Indique el correo:\n")
            self.Sexo =input("Indique su sexo:\n")
            self.Cedula = int(input("Indique la cedula: \n"))
            self.Celular = int(input("Indique su numero de celular: \n"))
            self.Rol =int(input("Indique el Id del rol que cumple: \n"))
            self.Comunicacion = int(input("Indique el Id de la comunicacion que se realizo: \n"))
            self.Efectividad = int(input("Indique el Id de la efectividad de la comunicacion: \n"))
            self.Mensaje = int(input("Indique el id de el mensaje enviado: \n"))
        except ValueError:
            print("Deben ingresarse numeros o usted tiene espacios en blanco ")
        else:
            sql = "update personas set Nombres = '{}',Apellidos = '{}' ,Cedula = '{}', Celular = '{}' , Email = '{}' , Sexo = '{}' ,IdRol ='{}' ,IdComunicacion ='{}' ,IdEfectividad = '{}' ,IdMensaje ='{}' where Id = '{}'".format(self.Nombres,self.Apellidos,self.Cedula,self.Celular,self.Email,self.Sexo,self.Rol,self.Comunicacion,self.Efectividad,self.Mensaje,self.Id)
            self.cursor.execute(sql)
            print("Elemento actualizado")
            self.conn.commit()
        os.system('pause')