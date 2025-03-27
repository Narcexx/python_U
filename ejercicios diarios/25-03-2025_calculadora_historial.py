def menu():
    print("---- Menu ----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Ver historial")
    print("6. Salir")

def numeros():
    while True:
        try:
            numero1 = int(input("Ingrese numero 1: "))
            numero2 = int(input("Ingrese numero 2: "))
            return numero1, numero2
        except ValueError:
            print("ERROR: Ingrese un numero")

historial = ""
def operaciones_y_historial(op, n1, n2):
    global historial
    if op == 1:
        resultado = n1 + n2
        historial += f"{n1} + {n2} = {resultado}\n"
    elif op == 2:
        resultado = n1 - n2
        historial += f"{n1} - {n2} = {resultado}\n"
    elif op == 3:
        resultado = n1 * n2
        historial += f"{n1} * {n2} = {resultado}\n"
    elif op == 4:
        if n2 == 0:
            return "No se puede dividir por cero"
        resultado = n1 / n2
        historial += f"{n1} / {n2} = {resultado}\n"
    return resultado
    
def ejecutar():
    global historial
    menu()
    while True:
        try:
            op = int(input("Ingrese opcion: "))
            if op == 6:
                break
            elif op in [1, 2, 3, 4]:
                num1, num2 = numeros()
                resultado = operaciones_y_historial(op, num1, num2)
                if resultado is not None:
                    print(f"Resultado: {resultado}\n")
            elif op == 5:
                print(f"Historial:\n{historial}")

            else:
                print("ERROR: Ingrese opcion valida")
        except ValueError:
            print("ERROR: Ingrese valor valido")

ejecutar()