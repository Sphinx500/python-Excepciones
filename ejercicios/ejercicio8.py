"""
Realiza un programa en el cual vas a solicitar dos números con los cuales realizamos las operaciones + - * /, estos números deben de ser de tipo entero, controlar los distintos errores mediante una excepción encadenada. (TypeError, ValueError,  ZeroDivisionError, etc.).

"""

class Calculadora:
    def __init__(self):
        self.valor1=int(input("Digita el valor 1: "))
        self.valor2=int(input("Digita el valor 2: "))

    def suma(self):
        try:
            suma = self.valor1 + self.valor2
            print("La suma es: ", suma)
        except TypeError:
            print("El tipo de valores no coinciden, no es posible hacer la operacion")
        except ValueError:
            print("No es posible hacer la operacion")
    
    def resta(self):
        try:
            resta = self.valor1 - self.valor2
            print("La resta es: ", resta)
        except TypeError:
            print("El tipo de valores no coinciden, no es posible hacer la operacion")
        except ValueError:
            print("No es posible hacer la operacion")

    def multiplicar(self):
        try:
            multi = self.valor1 * self.valor2
            print("La multiplicacion es: ", multi)
        except TypeError:
            print("El tipo de valores no coinciden, no es posible hacer la operacion")
        except ValueError:
            print("No es posible hacer la operacion")

    def dividir(self):
        try:
            divide = self.valor1 / self.valor2
            print("La division es: ", divide)
        except TypeError:
            print("El tipo de valores no coinciden, no es posible hacer la operacion")
        except ZeroDivisionError:
            print("No es posible dividir entre 0")
        except ValueError:
            print("No es posible hacer la operacion")

Calculadora()