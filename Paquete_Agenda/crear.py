from io import UnsupportedOperation


def agregaDatos():
        nombre = input("Ingresa un nombre: ")
        telefono = int(input("Ingresa un numero de telefono: "))
        archivo = "Paquete_Agenda/agendaTelefonos.txt"
        try: 
            with open(archivo) as f:
                datos = f.readlines()
                for i in datos:
                    if str(telefono) in i:
                        print("El telefono ya existe")
                else:
                    file = open(archivo,'a')
                    file.write(str(nombre) + '|' + str(telefono) + '\n')
                    file.close()
                    print('El teléfono se ha añadido.\n')
        except FileNotFoundError:
            print('¡El fichero ' + archivo + ' no existe!\n')
        except UnsupportedOperation:
            print("Operacion no permitida")
        


