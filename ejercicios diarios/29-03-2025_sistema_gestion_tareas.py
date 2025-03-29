# Me rendi solo hice las 2 primeras funciones y le pedi ayuda a ChatGPT y que me explicara paso a paso

def menu():
    print("\n---- MENU ----")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def agregar_tarea(tareas):
    nombre = input("Ingrese la tarea: ").strip()
    tarea = (nombre, "Pendiente")  # Se guarda como una tupla (nombre, estado)
    tareas.append(tarea) # Agrega la tupla a la lista tareas
    print(f"Tarea '{nombre}' agregada.")


def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    print("\n---- Lista de tareas ----")
    for i, (nombre, estado) in enumerate(tareas, start=1): # Usa enumerate(tareas, start=1) para numerarlas desde 1 en vez de 0.
        print(f"{i}. {nombre} - {estado}")


def marcar_completada(tareas):
    ver_tareas(tareas)
    if not tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea completada: ")) - 1
        if 0 <= indice < len(tareas):
            nombre, _ = tareas[indice]  # Extrae el nombre de la tarea
            tareas[indice] = (nombre, "Completada")  # Reemplaza la tupla con estado "Completada"
            print(f"Tarea '{nombre}' marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if not tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            nombre, _ = tareas.pop(indice)  # Extrae y elimina la tarea de la lista
            print(f"Tarea '{nombre}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")


def ejecutar():
    tareas = []  # Lista de tuplas donde guardamos las tareas
    while True:
        menu()
        try:
            op = int(input("¿Qué desea hacer?: "))
            if op == 5:
                print("\nHASTA LUEGO\n")
                break
            elif op == 1:
                agregar_tarea(tareas)
            elif op == 2:
                ver_tareas(tareas)
            elif op == 3:
                marcar_completada(tareas)
            elif op == 4:
                eliminar_tarea(tareas)
            else:
                print("ERROR: Elija una opción válida.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")


ejecutar()