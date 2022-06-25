from crear import agregaDatos
from menu import menu
from consultar import mostrarDatos
from eliminar import eliminarDatos
from crea_archivo import crear_archivo

while True:
    menu()
    try:
        op=int(input("Elija la operacion a realizar: "))
        if op == 1:
            crear_archivo()
        if op == 2:
            agregaDatos()
        elif op == 3:
            mostrarDatos()
        elif op == 4:
            eliminarDatos()
        elif op == 5:
            break
        else:
            print("Por favor elige una opcion")
            op=int(input("Elija la operacion a realizar: "))

    except ValueError:
        print("Solo se aceptan numeros del 1 al 5")

    except TypeError:
            print("Parametro no aceptado")