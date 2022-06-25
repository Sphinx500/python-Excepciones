def mostrarDatos():
    try:
        archivo = "Paquete_Agenda/agendaTelefonos.txt"
        telefono = input("telefono a buscar: ")
        with open(archivo) as f:
            datafile = f.readlines()
        for line in datafile:
            if telefono in line:
                print(line)
            else:
                break
    except FileNotFoundError:
            return('¡El fichero ' + archivo + ' no existe!\n')
    except ValueError:
        print("Solo se aceptan numeros")
    except TypeError:
        print("Argumento no valido")

