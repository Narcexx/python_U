import random
numero_random = random.randint(1, 10)
print("Adivine el numero entre 1 y 10")
while True:
    numero_user = int(input("Ingrese un numero: "))
    if numero_user > numero_random:
        print("Es menor")
    elif numero_user < numero_random:
        print("Es mayor")
    else:
        print("ADIVINASTE!")
        break