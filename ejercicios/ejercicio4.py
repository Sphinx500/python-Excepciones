"""
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución
"""

try:
    resultado = 15 + "20"
except TypeError:
    print("Los tipos de datos no coinciden, no es posible hacer la operacion")
finally:
    print("Se procede a convertir de str a int")
    resultado = 15 + int("20")
    print("Resultado: ", resultado)
