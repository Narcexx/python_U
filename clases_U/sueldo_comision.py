sueldo=210000
comision=0
categoria=int(input("Ingrese su categoria: "))
if categoria==1:
    comision=500000
elif categoria==2:
    comision=100000
elif categoria==3:
    comision=50000
elif categoria==4:
    comision=10000
else:
    print("NO ESTA ESA CATEGORIA")
print("Sueldo + comision es: ", sueldo+comision) #TAMBIEN PUEDE SER print(f"Sueldo + comision es: {sueldo+comision}")
    