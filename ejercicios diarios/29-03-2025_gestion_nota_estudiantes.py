def menu():
    print("\n---- MENU ----")
    print("1. Agregar nota")
    print("2. Ver todas las notas")
    print("3. Promedio de notas")
    print("4. Salir")


def agregar_nota(notas):
    while True:
        try:
            nota = float(input("Ingrese nota: "))
            if 0 <= nota <= 7: 
                notas.append(nota)
                break
            else:
                print("ERROR: La nota debe estar entre 0 y 7.")
        except ValueError:
            print("ERROR: Ingrese un numero valido")


def ver_notas(notas):
    if notas:
        for nota in notas:
            print(nota)
    else:
        print("No hay notas")


def calcular_promedio(notas):
    if notas:
        promedio = sum(notas) / len(notas)
        return f"El promedio de las notas es: {promedio}"
    else:
        return "No hay notas"
    

def ejecutar():
    notas = []
    while True:
        menu()
        try:
            op = int(input("Que desea hacer?: "))
            if op == 4:
                print("\nHASTA LUEGO\n")
                break
            elif op == 1:
                agregar_nota(notas)
            elif op == 2:
                ver_notas(notas)
            elif op == 3:
                print(calcular_promedio(notas))
            else:
                print("ERROR: Elija opcion valida")
        except ValueError:
            print("ERROR: Ingrese una opcion numerica")

ejecutar()