def monto_cuenta():
    while True:
        try:
            monto = float(input("Monto de la cuenta: "))
            if monto < 0:
                print("ERROR: Ingrese un monto valido")
            else:
                return monto
        except ValueError:
            print("ERROR: Ingrese un monto valido")

def porcentaje_propina():
    while True:
        try:
            porcentaje = float(input("Porcentaje de la propina: "))
            if porcentaje < 0 or porcentaje > 100:
                print("ERROR: Ingrese un porcentaje valido")
            else:
                return porcentaje
        except ValueError:
            print("ERROR: Ingrese un valor valido")

def calcular_cuenta(monto, porcentaje):
    propina = (monto * porcentaje) / 100
    cuenta_final = monto + propina
    return f"\nLa propina es de: {propina}\nTotal a pagar: {cuenta_final}" # Igual puede ser return propina, cuenta_final

def ejecutar():
    monto = monto_cuenta()
    porcentaje = porcentaje_propina()
    # propina, total = calcular_cuenta(monto, porcentaje)
    print(calcular_cuenta(monto, porcentaje)) # f"\nLa propina es de: {propina}\nTotal a pagar: {total}"

ejecutar()



