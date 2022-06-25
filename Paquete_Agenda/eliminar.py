def eliminarDatos():
    try:
        archivo = "Paquete_Agenda/agendaTelefonos.txt"
        f = open(archivo, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + archivo + ' no existe!\n')
    else:
        nombre=input("Ingresa el nombre a eliminar: ")
        data = f.readlines()
        print(data)
        f.close()
        data = dict([tuple(line.split('|')) for line in data])
        if nombre in data:
            del data[nombre]
            f = open(archivo, 'w')
            for nombre, telefono in data.items():
                f.write(nombre + '|' + telefono)
            f.close()
            print ('¡El cliente se ha borrado!\n')
        else:
            print('¡El cliente no existe!\n')
