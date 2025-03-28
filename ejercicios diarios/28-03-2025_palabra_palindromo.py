def ingresa_palabra():
    palabra = input("Ingrese palabra o frase: ").lower().replace(" ", "") # El replace() lo use para sacar los espacios en caso de una frase
    return palabra

def verificar_palindromo(palabra):
    i = 0
    j = len(palabra) - 1
    while i < j:
        if palabra[i] != palabra[j]:
            return False
        i += 1
        j -= 1
    return True

def ejecutar():
    palabra = ingresa_palabra()
    if verificar_palindromo(palabra):
        print("Es un palindromo")
    else:
        print("No es un palindromo")

ejecutar()