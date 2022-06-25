
def mostrar():
    try:
        with open('Paquete_Data\palabras.txt') as file:
            datafile = file.readlines()
            for i in range(0, len(datafile), 5):
                enter = input("Presione enter")
                if enter == ' ':
                    print(datafile[i:i + 5])
                else:
                    print("no fue posible continuar")

    except:
        print("ups algo salio mal")

