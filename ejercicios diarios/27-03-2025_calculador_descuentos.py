def precio_producto():
    while True:
        try:
            precio_prod = float(input("Ingrese el precio original: "))
            if precio_prod < 0:
                print("ERROR: Ingrese valor valido")
            else:
                return precio_prod
        except ValueError:
            print("ERROR: Ingrese numero valido")

def descuento():
    while True:
        try:
            desc = float(input("Ingrese el porcentaje de descuento: "))
            if desc > 100 or desc < 0:
                print("ERROR: Ingrese descuento valido")
            else:
                return desc
        except ValueError:
            print("ERROR: Ingrese valor valido")

def calcular_descuento(precio, porcentaje):
    descuento_aplicado = precio - ((precio * porcentaje) / 100)
    return f"El precio final con descuento es: {descuento_aplicado}"

def ejecutar():
    while True:
        precio = precio_producto()
        porcentaje = descuento()
        print(calcular_descuento(precio, porcentaje))
        op = input(f"\nDesea calcular otro descuento? (s/n): ").lower()
        if op == 'n':
            print("Saliendo...")
            break
        elif op != 's':
            print("ERROR: Ingrese 's' para continuar o 'n' para salir")

ejecutar()

