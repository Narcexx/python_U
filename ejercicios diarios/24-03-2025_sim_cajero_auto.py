saldo = 0
def menu():
    print("\n---- Cajero Automatico ----")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

# def obtener_monto(mensaje):  TAMBIEN PODIA SER CON UNA FUNCION PARA VALIDAR EL MONTO QUE SE INGRESE YA SEA DEPOSITO O RETIRO
#     """Solicita un monto y valida la entrada"""
#     while True:
#         try:
#             monto = float(input(mensaje))
#             if monto < 0:
#                 print("ERROR: No puedes ingresar valores negativos.")
#             else:
#                 return monto
#         except ValueError:
#             print("ERROR: Ingrese un número válido.")

def deposito():
    while True:
        try:
            dinero_depos = int(input("Ingrese cantidad a depositar: "))
            return dinero_depos
        except ValueError:
            print("ERROR: Ingrese numeros")

def retiro():
    while True:
        try:
            dinero_retiro = int(input("Ingrese cantidad a retirar: "))
            return dinero_retiro
        except ValueError:
            print("ERROR: Ingrese numeros")

def calculos(op, cantidad):
    global saldo  
    if op == 1:
        saldo += cantidad
        return f"Deposito exitoso. Saldo actual: {saldo}\n"
    elif op == 2:
        if saldo - cantidad < 0:
            return "No puede retirar esa cantidad\n"
        saldo -= cantidad
        return f"Retiro exitoso. Saldo actual: {saldo}\n"
    elif op == 3:
        return f"Saldo actual: {saldo}\n"
    # if op == 1:
    #     saldo_actual = saldo + deposito
    #     mensaje = f"Deposito exitoso. Saldo actual: {saldo_actual}"
    # elif op == 2:
    #     if saldo - retiro < 0:
    #         return "No puede retirar mas dinero"
    #     else:
    #         saldo_actual = saldo - retiro
    #         mensaje = f"Retiro exitoso. Saldo actual: {saldo_actual}"
    # elif op == 3:
    #     return f"Saldo actual: {saldo_actual}\n"
    # return mensaje
        
def ejecutar():
    while True:
        try:
            op = int(input("Ingrese opcion: "))
            if op == 4:
                print("Saliendo...")
                break
            elif op == 1:
                print(calculos(op, deposito()))
            elif op == 2:
                print(calculos(op, retiro()))
            elif op == 3:
                print(calculos(op, 0))
            else:
                print("Ingrese una opcion valida\n")
        except ValueError:
            print("ERROR: Ingrese un numero valido\n")

menu()
ejecutar()