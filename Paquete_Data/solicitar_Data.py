
def carga():

    try:
        with open('Paquete_Data\palabras.txt', 'w') as a:
            for i in range(10):
                frase = input("Ingrese una frase: ")
                a.write(frase + '\n')
    except IndexError:
        print("Fuera de rango")
    except OSError:
        print("No fue posible abrir el archivo o no existe")

    try:
        data = []
        with open('Paquete_Data\palabras.txt') as file:
            for lineas in file:
                data.extend(lineas.split())
            print(data)
            palabras = data
    except OSError:
        print("No fue posible abrir el archivo o no existe")

    except KeyError:
        print("No fue posible agregar los elementos")
    
    except IndexError:
        print("Fuera de rango")
    
    finally:
        file.close()

