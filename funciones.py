from varglobal import ventastotales
from grafico import GraficoDinamico

import time

def Leerbasededatos():
    pass

def Guardarenbasededatos():
    pass


def registrarventas(dia):

    while True:
        nombre = input("Indique el nombre de el producto o escriba salir: ")
        if nombre == "salir":
            break
        try:
            venta = int(input("Indique el valor de el producto: "))


        except ValueError:
            break
        print("")
        ventasdias = ventastotales[dia-1]
        ventasdias.append((nombre, venta))


        
    

def mostrarventas(dia):
    while True:
        print(f"""
            ============== Eliga la opcion de su preferencia ===============
            1) Mostrar Todas las ventas 
            2) Mostrar Ventas del Dia: {dia}
                     o escriba salir
    
           """)
        opcion = input("Seleccione la opcion de su preferencia (1 o 2) o escriba salir: ")
        if opcion == "1":
            print(f"\n==== Listado de Ventas Totales  ====")
            i = 1
            for ventasxdia in ventastotales:
                retraso(0.2)
                print(f"\n      ===dia: {i}==     ")
                i += 1
                for ventas in ventasxdia:
                    retraso()
                    nombre = ventas[0]
                    valor = ventas[1]

                    print("\nNombre:", nombre, "Valor:", valor)


        elif opcion ==  "2": 
            print(f"\n==== Listado de Ventas del dia: {dia}  ====")

            ventasxdias = ventastotales[dia-1]
            for ventas in ventasxdias:
                retraso()

                nombre = ventas[0]
                valor = ventas[1]

                print("\nNombre:", nombre, "Valor:", valor)
        else: 
            break   

def estadisticas(dia):
    #VENTAS DEL DIA 
    
    ventasxdias = ventastotales[dia-1]
    sumaventas = 0
    for ventas in ventasxdias:
       sumaventas += ventas[1]
    try:
        promedio_dia= sumaventas/len(ventasxdias)
    except ZeroDivisionError:
        promedio_dia = 0
    print(f" el Promedio del este dia es: {promedio_dia}")

    sumaventas = 0
    i= 1
    for ventasxdia in ventastotales:
        for ventas in ventasxdia:
           i += 1
           sumaventas += ventas[1]
        try:
            promediototal= sumaventas/i
        except ZeroDivisionError:
            promediototal = 0
    print(f" el Promedio del este total es: {promediototal}")
    diferencia = abs(promediototal-promedio_dia)
    if promedio_dia<promediototal:
        print(f"el promedio del dia es menor al promedio total, la diferencia es de: {diferencia}")
    elif promediototal<promedio_dia:
        print(f"el promedio del dia es mayor al promedio total, la diferencia es de: {diferencia}")

    if input("desea ver un grafico con los promedios? si/no").lower() == "si":

        i = 1
        y = []
        for ventasxdia in ventastotales:
                i += 1
                ventasdeldia = 0
                for ventas in ventasxdia:
                    ventasdeldia += ventas[1]
                y.append(ventasdeldia)
        if y:
            grafico = GraficoDinamico(y)
        else:
            print("ERROR: NO HAY DATOS")

                     
def retraso(x = 0.3):
    time.sleep(x)
               


