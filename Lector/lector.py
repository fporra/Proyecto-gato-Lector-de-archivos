def contador(nombre_archivo):
    contador_letras = 0
    contador_espacios = 0
    with open(nombre_archivo, "r") as f:
        contenido = f.read()

        for caracter in contenido:
            if caracter.isalpha():
                contador_letras += 1
            elif caracter.isspace():
                contador_espacios += 1
    return contador_letras, contador_espacios

nombre_archivo = "dato2.txt"
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    total_letras, total_espacios = contador(nombre_archivo)
    print("Cantidad de letras en el archivo:", total_letras)
    print("Cantidad de espacios en el archivo:", total_espacios)

print("Contenido del archivo:")
print(contenido)
