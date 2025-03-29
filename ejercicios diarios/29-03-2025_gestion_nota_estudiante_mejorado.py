def menu():
    print("\n---- MENU ----")
    print("1. Agregar nota")
    print("2. Ver todas las notas")
    print("3. Promedio de notas")
    print("4. Eliminar nota")
    print("5. Ordenar notas mayor a menor")
    print("6. Salir")


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
            print(f"- {nota}")
    else:
        print("No hay notas")


def calcular_promedio(notas):
    if notas:
        promedio = sum(notas) / len(notas)
        return f"El promedio de las notas es: {promedio}"
    else:
        return "No hay notas"
    

def eliminar_nota(notas):
    while True:
        try:
            ver_notas(notas)
            nota_eliminar = float(input("Cual desea eliminar?: "))
            if nota_eliminar in notas:
                notas.remove(nota_eliminar)
                print(f"'{nota_eliminar}' se elimino")
                break
            else:
                print("No esta esa nota")
                break
        except ValueError:
            print("ERROR: Ingrese una nota")


def ordenar_notas(notas):
    # return notas.sort(reverse=True) # ESTA LINEA LA AGRUEGUE POR CONSEJO DE CHATGPT, ya que el return estaba mal
    if notas:
        notas.sort(reverse=True)
        print("Notas ordenadas de mayor a menor:")
        ver_notas(notas)
    else:
        print("No hay notas registradas.")

# def guardar_notas(notas): # Esta funcion es para guardar las notas en un archivo de texto, me lo dio ChatGPT
#     if notas:
#         with open("notas.txt", "w") as archivo:
#             for nota in notas:
#                 archivo.write(str(nota) + "\n")
#         print("Notas guardadas en 'notas.txt'.")
#     else:
#         print("No hay notas para guardar.")


def ejecutar():
    notas = []
    while True:
        menu()
        try:
            op = int(input("Que desea hacer?: "))
            if op == 6:
                print("\nHASTA LUEGO\n")
                break
            elif op == 1:
                agregar_nota(notas)
            elif op == 2:
                ver_notas(notas)
            elif op == 3:
                print(calcular_promedio(notas))
            elif op == 4:
                eliminar_nota(notas)
            elif op == 5:
                ordenar_notas(notas)
            else:
                print("ERROR: Elija opcion valida")
        except ValueError:
            print("ERROR: Ingrese una opcion numerica")

ejecutar()

# Una manera de hacer el ejecutar() que me dio el ChatGPT usando un diccionario (el cual todavia no he visto por eso no lo use)
# def ejecutar():
#     notas = []
#     opciones = {
#         1: agregar_nota,
#         2: ver_notas,
#         3: lambda notas: print(calcular_promedio(notas)),
#         4: eliminar_nota,
#         5: ordenar_notas,
#     }

#     while True:
#         menu()
#         try:
#             op = int(input("¿Qué desea hacer?: "))
#             if op == 6:
#                 print("\nHASTA LUEGO\n")
#                 break
#             elif op in opciones:
#                 opciones[op](notas)
#             else:
#                 print("ERROR: Elija una opción válida.")
#         except ValueError:
#             print("ERROR: Ingrese un número válido.")