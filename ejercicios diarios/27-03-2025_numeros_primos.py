def ingresa_numero():
    while True:
        try:
            numero = int(input("Ingresa numero: "))
            if numero > 0:
                return numero
        except ValueError:
            print("ERROR: Ingresa un numero")

def primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if  numero % i == 0:
            return False
    return True

def ejecutar():
    numero = ingresa_numero()
    if primo(numero):
        print(f"Es primo el numero: {numero}")
    else:
        print(f"No es primro el numero: {numero}")

ejecutar()
            