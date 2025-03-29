for numero in range(5):
    print(numero)

print("\n")
buscar = 10
for numero in range(5): #for-else
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("no se encontro el numero")

print("\n")
for char in "No se que escribir aca":
    print(char)

print("\n")
lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
for lenguaje in lenguajes:
    print(lenguaje)

print("\n")
#loop anidado
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")