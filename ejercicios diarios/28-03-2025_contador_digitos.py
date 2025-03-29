def input_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            if numero > 0:
                return numero
            else:
                print("ERROR: Ingrese un numero positivo")
        except ValueError:
            print("ERROR: Ingrese un numero")
        

def contador(numero):
    return len(str(numero))


def ejecutar():
    numero= input_numero()
    print(f"El numero {numero} tiene {contador(numero)} digitos")


ejecutar()