# def menu():
#     print("---- Menu ----")
#     print("1.Suma")
#     print("2.Resta")
#     print("3.Multiplicacion")
#     print("4.Division")
#     print("5.Salir")

# def operacion():
#     n1 = int(input("Ingrese numero 1: "))
#     n2 = int(input("Ingrese numero 2: "))

# def opcion():
#     operacion()
#     while True:
#         op = int(input("Ingrese opcion: "))
#         if op == 1:
#             resultado = n1 + n2
#         elif op == 2:
#             resultado = n1 - n2
#         elif op == 3:
#             resultado = n1 * n2
#         elif op == 4:
#             resultado = n1 / n2
#         elif op == 5:
#             break
#         else:
#             print("Ingrese opcion valida")

# menu()
# opcion()
def menu():
    print("---- Menú ----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def numeros():
    n1 = float(input("Ingrese número 1: "))
    n2 = float(input("Ingrese número 2: "))
    return n1, n2  # Se retornan los valores

def calcular(op, n1, n2):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        return n1 / n2 
    
def ejecutar():  # Función principal
    while True:
        menu()
        op = int(input("Ingrese opción: "))
        if op == 5:
            break
        if op in [1, 2, 3, 4]: # Igual puede ser if op == 1 or op == 2 or op == 3 or op == 4:
            n1, n2 = numeros()
            print(f"El resultado es: {calcular(op, n1, n2)}\n")
        else:
            print("Ingrese una opción válida\n")

ejecutar()