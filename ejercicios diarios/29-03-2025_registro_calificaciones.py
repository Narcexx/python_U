def menu():
    print("\n---- MENU ----")
    print("1. Agregar alumno y notas")
    print("2. Ver lista de alumnos y notas")
    print("3. Calcular promedio de un alumno")
    print("4. Mostrar alumno con la nota mas alta")
    print("5. Salir")


def pedir_nota():
    """Solicita una nota válida entre 1.0 y 7.0 al usuario."""
    while True:
        try:
            nota = float(input("Ingrese una nota (1.0 - 7.0): "))
            if 1.0 <= nota <= 7.0:
                return nota
            else:
                print("ERROR: La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")


def agregar_alumno(lista_alumnos):
    """Agrega un alumno y sus notas a la lista."""
    nombre = input("Ingrese el nombre del alumno: ").strip().capitalize()
    
    while True:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de notas: "))
            if cantidad_notas > 0:
                break
            else:
                print("ERROR: La cantidad de notas debe ser mayor a 0.")
        except ValueError:
            print("ERROR: Ingrese un número entero válido.")
    
    notas = [pedir_nota() for _ in range(cantidad_notas)]  # List Comprehension para obtener notas
    
    lista_alumnos.append((nombre, notas))  # Se almacena como tupla (nombre, lista de notas)
    print(f"Alumno '{nombre}' agregado con éxito.")


def ver_alumnos(lista_alumnos):
    """Muestra la lista de alumnos y sus notas."""
    if not lista_alumnos:
        print("No hay alumnos registrados.")
        return
    
    print("\n---- Lista de Alumnos y Notas ----")
    for i, (nombre, notas) in enumerate(lista_alumnos, start=1):
        notas_str = ", ".join(map(str, notas))  # Convierte las notas en una cadena separada por comas
        print(f"{i}. {nombre}: {notas_str}")


def calcular_promedio_alumno(lista_alumnos):
    """Calcula el promedio de notas de un alumno específico."""
    nombre = input("Ingrese el nombre del alumno: ").strip().capitalize()
    
    for alumno, notas in lista_alumnos:
        if alumno == nombre:
            promedio = sum(notas) / len(notas)
            print(f"\nEl promedio de {nombre} es: {promedio:.2f}")
            return
    
    print(f"No se encontró al alumno '{nombre}'.")


def mostrar_alumno_nota_mas_alta(lista_alumnos):
    """Muestra el alumno con la nota más alta."""
    if not lista_alumnos:
        print("No hay alumnos registrados.")
        return
    
    alumno_mayor = max(lista_alumnos, key=lambda x: max(x[1]))  # Encuentra el alumno con la nota más alta
    nombre, notas = alumno_mayor
    nota_maxima = max(notas)
    
    print(f"\nEl alumno con la nota más alta es '{nombre}' con una nota de {nota_maxima}.")


def ejecutar():
    """Función principal que ejecuta el programa."""
    lista_alumnos = []
    
    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregar_alumno(lista_alumnos)
            elif opcion == 2:
                ver_alumnos(lista_alumnos)
            elif opcion == 3:
                calcular_promedio_alumno(lista_alumnos)
            elif opcion == 4:
                mostrar_alumno_nota_mas_alta(lista_alumnos)
            elif opcion == 5:
                print("HASTA PRONTO")
                break
            else:
                print("ERROR: Opción inválida.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")

ejecutar()


