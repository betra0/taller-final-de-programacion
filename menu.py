
from funciones import *
from varglobal import ventastotales, agregardia

while True:

    print
    dia = len(ventastotales)
    #print(ventastotales)
    # Sobreescribir base de datos
    print(f"""
            ================= Chaparritos Corp ====================
            Dia: {dia}

            1) Registrar Ventas 
            2) Mostrar Ventas 
            X) ver estadisticas de vetas(Proximamente)
            4) Dia siguiente
             O escriba salir para salir

    
           """)
    opcion = input("Seleccione la opcion de su preferencia (1, 2, 3 o 4): ")

    if opcion == "1":
        registrarventas(dia)
    elif opcion == "2":
        mostrarventas(dia)
        
    elif opcion == "3":
        estadisticas(dia)

    elif opcion == "4":
        agregardia()

    elif opcion == "salir":
        break

    else:
        print("\nERROR: Selecione una opcion valida\n")
    time.sleep(0.3)

        



