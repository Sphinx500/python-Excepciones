"""
Realiza una función llamada agregar_una_vez que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.
"""

def agregar_una_vez():
    lista= [1,2,3,4,5]

    try:
        elemento = int(input("Inserte elemento: "))
        if elemento not in lista:
            lista.append(elemento)
        else:
            raise ValueError("Error: Imposible añadir elementos duplicados =>", elemento)
    except ValueError:
        raise
    finally:
        print(lista)


agregar_una_vez()