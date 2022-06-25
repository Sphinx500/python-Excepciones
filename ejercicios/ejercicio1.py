"""
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.
"""

try:
    divide = 10/ 0
except ZeroDivisionError:
    print("No es posible dividir entre 0, intente con otro numero")
finally:
    num=int(input(("Ingrese otro numero: ")))
    divide = 10/num
    print(divide)