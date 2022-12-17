from tabulate import tabulate
import pymysql
import os



class Fidelizacion:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='Pelusa24#',
            db='fidelizacion2'
        )

        self.cursor = self.conn.cursor()


    def Submenu(self):
        Salida = True
        while Salida == True:
            os.system("cls")
            print("Cual Resultado desea ver")
            print("1. Clientes Fidelizados")
            print("2. Cliente No Fidelizados")
            print("3. Volver al principal")
            try:
                opc = int(input("Indique la opcion deseada:\n"))
                if(opc == 1):
                    self.MostrarSi()
                elif(opc == 2):
                    self.MostrarNo()
                elif(opc == 3):
                    Salida = False
                else:
                    print("Opcion no diponible")
                    os.system("pause")
            except ValueError:
                print("Debe ingresar un numero")
                os.system("pause")


    def MostrarSi(self):
        os.system("cls")
        Aux = 1
        sql = "select * from personas where IdEfectividad = '{}'".format(Aux)
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id","Nombre","Apellidos","Cedula","Celular","Email","Sexo","IdRol","Comunicacion","Efectividad","Mensaje"]
        for row in rows:
            print(tabulate(row, headers = headers))
        os.system('pause')


    def MostrarNo(self):
        os.system("cls")
        Aux = 2
        sql = "select * from personas  where IdEfectividad ='{}'".format(Aux)
        self.cursor.execute(sql)
        rows = [self.cursor.fetchall()]
        headers = ["Id","Nombre","Apellidos","Cedula","Celular","Email","Sexo","Rol","Comunicacion","Efectividad","Mensaje"]
        for row in rows:
            print(tabulate(row, headers = headers))
        os.system('pause')
