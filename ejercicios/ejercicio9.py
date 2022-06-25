"""
Trata de abrir un archivo, en caso de que no exista este archivo se necesita controlar la excepción, en un bloque finally, cerramos el archivo para evitar desperdiciar recursos.
"""

try:
    with open('hola.txt') as file:
        lee = file.read()

except OSError:
    print("No fue posible abrir el archivo o no existe")

finally:
    file.close()