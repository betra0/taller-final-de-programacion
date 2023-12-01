from varglobal import ventastotales

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


                     
def retraso(x = 0.3):
    time.sleep(x)
               


