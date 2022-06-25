from menu import menu
from solicitar_Data import carga
from mostrar_Data import mostrar

while True:
    try:
        menu()
        op=int(input("Elija la operacion a realizar: "))
        if op == 1:
            carga()
        elif op == 2:
            mostrar()
        elif op == 3:
            break
        else:
            print("Por favor elige una opcion")
            op=int(input("Elija la operacion a realizar: "))

    except ValueError:
        print("Solo se aceptan numeros del 1 al 3")

    except TypeError:
            print("Parametro no aceptado")
