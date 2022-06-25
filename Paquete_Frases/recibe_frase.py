from guardar_excepciones import errores

def palabras():
    try:
        frase = input("Ingrese una frase: ")
        letra = input("Ingrese una letra: ")
        
        if(not letra.isalpha()):
            raise ValueError("La letra debe pertenecer al alfabeto")
        if(len(letra) > 1):
            raise ValueError("Solo es una letra")

        conteo = frase.count(letra)
        print("la letra: ", letra, " aparece: ", conteo)
    except ValueError as err:
        errores( str(err) + "\n")
    except TypeError as err:
        errores( str(err) + "\n")

