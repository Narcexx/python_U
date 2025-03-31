numeros = int(input("Ingrese cantidad de numeros a evaluar: "))
cont_par = 0
cont_impar = 0
cont = 1
while cont <= numeros:
    numero_input = int(input(f"Ingrese numero {cont}: "))
    if numero_input%2!=0:
        cont_impar +=1
    else:
        cont_par +=1
    cont +=1

print(f"Habian {cont_par} de pares")
print(f"Habian {cont_impar} de impares")