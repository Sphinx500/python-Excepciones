def crear_archivo():
    import os
    archivo = "Paquete_Agenda/agendaTelefonos.txt"
    if os.path.isfile(archivo):
        r = input('El fichero ' + archivo + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if r == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    f = open(archivo, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'

