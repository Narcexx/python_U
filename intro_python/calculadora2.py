#EJERCICIO DEL VIDEO HolaMundo min 2:33:30
print("Bienvenido a la calculadora")
print("Para salir escribe 'Salir'")
print("Las operaciones son suma, multi, div y resta")
numero1 = float(input("Ingrese numero: "))

while True:
    operacion = input("Ingrese operacion: ")
    if operacion.lower() == "suma" or operacion == "+":
        numero2 = float(input("Ingrese siguiente numero: "))
        resultado = numero1 + numero2
    elif operacion.lower() == "multi" or operacion.lower() == "x" or operacion == "*":
        numero2 = float(input("Ingrese siguiente numero: "))
        resultado = numero1 * numero2
    elif operacion.lower() == "div" or operacion.lower() == ":" or operacion == "/":
        numero2 = float(input("Ingrese siguiente numero: "))
        resultado= numero1 / numero2
    elif operacion.lower() == "resta" or operacion.lower() == "-":
        numero2 = float(input("Ingrese siguiente numero: "))
        resultado = numero1 - numero2
    elif operacion.lower().capitalize() == "Salir":
        break
    else:
        print("Operacion no valida")
        break

    numero1 = resultado
    print(f"El resultado es {resultado}")