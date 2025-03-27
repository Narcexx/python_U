print("\nQue operacion realizara\n1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n5.CERRAR")
respuesta = int(input())
while respuesta != 5:
    if respuesta == 1:
        numero = float(input("Ingrese numero: "))
        nuemro2 = float(input("Ingrese numero: "))
        resultado = numero + nuemro2
        print(f"\nRESULTADO = {resultado}")
    elif respuesta == 2:
        numero = float(input("Ingrese numero: "))
        nuemro2 = float(input("Ingrese numero: "))
        resultado = numero - nuemro2
        print(f"\nRESULTADO = {resultado}")
    elif respuesta == 3:
        numero = float(input("Ingrese numero: "))
        nuemro2 = float(input("Ingrese numero: "))
        resultado = numero * nuemro2
        print(f"\nRESULTADO = {resultado}")
    elif respuesta == 4:
        numero = float(input("Ingrese numero: "))
        nuemro2 = float(input("Ingrese numero: "))
        resultado = numero / nuemro2
        print(f"\nRESULTADO = {resultado}")
    else:
        print("NO ESTA ESA OPCION")
    
    print("\nQue operacion realizara\n1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n5.CERRAR")
    respuesta = int(input())
