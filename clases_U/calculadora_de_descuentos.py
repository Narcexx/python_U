p_producto = int(input("Ingrese precio del producto:"))
descuento = int(input("Ingrese el descuento: "))
if p_producto >= 0 and descuento >=0 and descuento <=100:
    print(f"El precio con el descuento es {(p_producto*descuento)/100}")
else:
    if p_producto < 0:
        print("Precio producto no valido")
    if descuento < 0:
        print("Descuento no valido")
