import random
numero_random = random.randint(1,100)
cont = 0
print("Adivina el numero entre 1 y 100")
while True:
    try:
        cont += 1
        num_usuario = int(input("Ingrese un numero: "))
        if num_usuario < numero_random:
            print("Muy bajo, intenta de nuevo")
        elif num_usuario > numero_random:
            print("Muy alto, intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el numero en {cont} intentos")
            break
    except ValueError:
        print("ERROR: Ingrese un numero.")
    