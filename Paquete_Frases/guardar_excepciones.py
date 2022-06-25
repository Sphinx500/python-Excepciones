
def errores(error):
    with open("Paquete_Frases\error.txt", "w") as f:
        f.write(error)
        f.close()