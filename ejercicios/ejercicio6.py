"""
Crea un programa que acceda a la posición que el usuario indique de la siguiente lista: [6,14,11,3,2,1,15,19]. No olvides capturar las excepciones que puedan surgir en caso de que el usuario introduzca un índice incorrecto o que no exista en la lista.
"""

lista = [6,14,11,3,2,1,15,19]

try:
    indice=int(input("Ingrese el indice al que desea acceder: "))
    print(lista[indice])

except IndexError:
    raise IndexError("Fuera de rango")

finally:
    print("la lista es la siguiente: ")
    print(lista)