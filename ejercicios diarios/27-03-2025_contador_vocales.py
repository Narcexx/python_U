def palabra():
    word = input("Ingrese una palabra o frase: ").lower()
    return word

def contador_vocales(palabra):
    contador = 0
    for i in palabra: #for-else
        if i in ['a', 'e', 'i', 'o', 'u']:
            contador += 1
    if contador == 0:
        print("No tiene vocales tu palabra o frase")
    return contador

word = palabra()
print(f"La cantidad de vocales: {contador_vocales(word)}")