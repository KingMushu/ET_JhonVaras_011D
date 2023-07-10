from datetime import datetime
import time
import os
import msvcrt
from pickle import GLOBAL

#Variables
flag=True
cantidadV=0
sw=1
vendidos=[]
matriz=[]
cont=1
AsientosV=[]
ValorA=0


def fecha(date): 
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"] 
    #["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    day = date.day 
    month = months[date.month - 1] 
    year = date.year 
    messsage = "{}/{}/{}".format(day, month, year,)
    return messsage
now = datetime.now() 

def IniciarPrograma():
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")

def menu():
    print(" ")
    print("*********************************************")
    print(" Bienvenido a nuestra productora de eventos! ")
    print("*********************************************")
    print("                  CREATIVOS.CL               ")
    print("---------------------------------------------")
    print("1 - Comprar asientos                         ")
    print("2 - Ubicaciones disponibles                  ")
    print("3 - Listado de asistentes                    ")
    print("4 - Ganancias totales                        ")
    print("5 - Salir                                    ")
    print("*********************************************")
    print("   ")

def opcion1():
    flag0=True
    flag=True
    flag2=True
    flag3=True
    flag4=True
    print("--Compra de entradas--")
    print("    ")
    global Cliente
    while flag==True:
        while flag0==True:
            print("--Rut de cliente--")
            print("  ")
            rut=input("Ingrese aqui ==> ")
            if len(rut) >= 8 and len(rut) <=9:
                print("")
                print("-Rut Registrado-")
                print(" ")
                os.system("cls")
                flag0=False
            else:
                print(" ")
                print("-Rut Invalido, intente nuevamente-")
                print(" ")
        os.system("cls")
        print("    ")
        print("--Cuantos asientos desea comprar?(MAX 3)--")
        while flag4==True:
            cantA=int(input("Ingrese aqui ==> "))
            if cantA == 0:
                flag2=False
                flag3=False
                flag4=False
                flag0=False
                flag=False
                break
            elif cantA > 3:
                print("--Cantidad invalida--")
                flag4=True
            elif cantA >=1 and cantA <=3:
                flag4=False
        if cantA > 1:
            print("ASIENTOS DISPONIBLES")
            print("  ")
            print("========================================")
            print("|                Escenario             |")
            print("========================================")
            for fila in matriz:
                print(f"{fila}")
        else:
            break
        ocupado=False
        while ocupado==False:
            for i in range (1,cantA+1):
                if cantA == 1:
                    print("     ")
                    print("--Escoja un asiento--")
                    print("   ")
                elif cantA > 1 and cantA <= 3:
                    print("     ")
                    print("--Escoja los asientos--")
                    print("   ")
                while flag3 == True:
                    Asiento=int(input(f"Ingrese asiento {i} aqui ==> "))
                    print("   ")
                    if Asiento >= 1 and Asiento <=20:
                        ValorA=120000
                        flag3=False
                    if Asiento >=21 and Asiento <=50:
                        ValorA=80000
                        flag3=False
                    if Asiento >=51 and Asiento <=100:
                        ValorA=50000
                        flag3=False
                    if Asiento > 100:
                        print("Asiento no existe")
                        print("  ")
                        print("========================================")
                        print("|                Escenario             |")
                        print("========================================")
                        print(f"{fila}")
                        print(" ")
                        flag3=True
                for a in vendidos:
                    if Asiento==a:
                        ocupado=True
                    else:
                        ocupado=False
                if ocupado==True:
                        print("--Asiento ya ocupado, elija otro--")
                        print("   ")
                        break
                elif ocupado==False:
                    for i in range(10):
                        for j in range(10):
                            if matriz[i][j]==Asiento:
                                ocupado=False
                                print("Asiento Disponible")
                                print("  ")
                                flag2=True
                                while flag2==True:
                                    print("--Desea comprarlo?(si/no)--")
                                    print("  ")
                                    respuesta=input("Ingrese aqui ==> ")
                                    print("   ")
                                    respuesta=respuesta.lower()
                                    if respuesta=='si':
                                        matriz[i][j]="X"
                                        vendidos.append(Asiento)
                                        Cliente={"Rut": rut, "Asiento": Asiento, "Valor del asiento": ValorA }
                                        AsientosV.append(Cliente)
                                        print("--Asiento comprado--")
                                        print("  ")
                                        print("========================================")
                                        print("|                Escenario             |")
                                        print("========================================")
                                        for fila in matriz:
                                            print(f"{fila}")
                                        print("  ")
                                        flag2=False
                                        flag3=True
                                        ocupado=True
                                    elif respuesta=='no':
                                        ocupado=True
                                        flag2=False
                                        flag3=True
                                    else:
                                        print("Escriba solo si o no")
                                        print("  ")
        print("--Desea comprar otra entrada?(si/no)--")
        print("     ")
        respuesta=input("Ingrese aqui ==> ")
        print("  ")
        respuesta=respuesta.lower()
        if respuesta=='no':
            os.system("cls")
            break
        elif respuesta != 'no':
            flag=True
            flag2=True
            flag3=True
            flag0=True
        os.system("cls")

def opcion2():
    print("--Asientos Disponibles--")
    print("  ")
    print("========================================")
    print("|                Escenario             |")
    print("========================================")
    for fila in matriz:
        print(fila)
    print(" ")
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")

def opcion3():
    print("--Listado de asistentes--")
    print("   ")
    clientes_ordenados = sorted(AsientosV, key=lambda x: x["Rut"])
    for Cliente in clientes_ordenados:
        print(f"Rut: {Cliente['Rut']} || Asiento: {Cliente['Asiento']} || Valor del asiento: {Cliente['Valor del asiento']}")
    print(" ")
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")

def opcion4():
        cantidad_vendidos1 = sum(1 for cliente in AsientosV if cliente["Asiento"] in range(1, 21))
        cantidad_vendidos2 = sum(1 for cliente in AsientosV if cliente["Asiento"] in range(21, 51))
        cantidad_vendidos3 = sum(1 for cliente in AsientosV if cliente["Asiento"] in range(51, 101))
        valor_total1 = sum(Cliente["Valor del asiento"] for Cliente in AsientosV if Cliente["Asiento"] in range(1, 21))
        valor_total2 = sum(Cliente["Valor del asiento"] for Cliente in AsientosV if Cliente["Asiento"] in range(21, 51))
        valor_total3 = sum(Cliente["Valor del asiento"] for Cliente in AsientosV if Cliente["Asiento"] in range(51, 101))
        valor_totalT = sum(Cliente["Valor del asiento"] for Cliente in AsientosV if Cliente["Asiento"] in range(1, 101))
        if valor_totalT > 0:
            for i in range(0,110,30):
                print(f"Cargando Ganancias...{i}%")
                time.sleep(1)
                os.system("cls") 
            print("--Ganancias Totales--")
            print("  ")
            print("*************************************************")
            print("| Tipo    | Precios | Cantidad Entradas | Total |")
            print(f"|Platinum | $120000 |         {cantidad_vendidos1}         | ${valor_total1} |")
            print(f"|Gold     | $80000  |         {cantidad_vendidos2}         | ${valor_total2} |")
            print(f"|Silver   | $50000  |         {cantidad_vendidos3}         | ${valor_total3} |")
            print("---------------------------------------------- ")
            print(f"                                 Total: ${valor_totalT}")
            print("*************************************************")
            print(" ")
            print("Presione para continuar...")
            msvcrt.getch()
            os.system("cls")
        else:
            print("--No hay ganancias--")
            print(" ")
            print("Presione para continuar...")
            msvcrt.getch()
            os.system("cls")




#Matriz
for i in range(10):
    fila=[]
    for j in range(10):
        fila.append(cont)
        cont+=1
    matriz.append(fila)



IniciarPrograma()
while sw==1:
    try:
        menu()
        opcion=int(input("Ingrese una opcion:"))
        os.system("cls")
        print("    ")
        if opcion==1:
            opcion1()
        if opcion==2:
            opcion2()
        if opcion==3:
            opcion3()
        if opcion==4:
            opcion4()
        if opcion==5:
            for i in range(5,0,-1):
                print
                print(f"Saliendo en...{i}")
                time.sleep(1)
                os.system("cls")
            print(f"Jhon Varas    Fecha: {fecha(now)}")
            sw=0
    except:
        print("Error, Ingrese nuevamente")