def menu():
    print("---- Menu ----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Mostrar ultimo resultado")
    print("6. Salir")

def numeros():
    while True:
        try:
            n1 = float(input("\nIngresa el primer numero: "))
            n2 = float(input("Ingresa el segundo numero: "))
            return n1, n2
        except ValueError:
            print("Error: Ingresa numeros validos")

def operaciones(op, num1, num2):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        if num2 == 0:
            return "No se puede dividir por cero"
        return num1 / num2
    
def ejecutar():
    ultimo_resultado = None
    while True:
        try:
            op = int(input("Ingrese opcion: "))
            if op == 6:
                print("Saliendo...")
                break
            elif op in [1, 2, 3, 4]: # Igual puede ser if op == 1 or op == 2 or op == 3 or op == 4:
                n1, n2 = numeros()
                ultimo_resultado = operaciones(op, n1, n2) 
                print(f"Resultado: {ultimo_resultado}\n") 
            elif op == 5:
                if ultimo_resultado == None:
                    print("No hay resultados previos")
                else:
                    print(f"Ultimo resultado: {ultimo_resultado}\n")
            else:
                print("Ingrese una opcion valida\n")
        except ValueError:
            print("ERRO: Ingrese un numero valido\n")

menu()
ejecutar()