"""
Crea una aplicación que reciba la clave de un diccionario y acceda a uno de sus valores. Asegúrate de que capturas las excepciones que puedan saltar al intentar acceder a una clave del diccionario inexistente.

"""

def dic():
    frutas = {'platano':'banana','manzana':'apple','uva':'grapes'}
    try:
        valor = input("Ingrese el valor al cual queremos acceder: ")
        print(frutas[valor])
    except KeyError:
        print("El valor no existe")

dic()