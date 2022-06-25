"""
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución

"""

try:
    lista = [1,2,3,4,5]
    lista [10]
except IndexError:
    print("Se encuentra fuera de rango")
finally:
    for i in range(6):
        num = int(input("Agrega un elemento en la posición faltante: "))
        lista.append(num)
    print(lista)
    print(lista[10])