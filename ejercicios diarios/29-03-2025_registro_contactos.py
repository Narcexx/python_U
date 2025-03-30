def menu():
    print("\n---- MENU ----")
    print("1. Agregar un contacto(nombre y numero telefono)")
    print("2. Ver lista de contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def agregar_contacto(lista_contactos):
    nombre_contacto = input("Ingrese nombre contacto: ").lower().capitalize()
    numero_telefono = int(input("Ingrese numero telefono: "))
    contacto = (nombre_contacto, numero_telefono)
    lista_contactos.append(contacto)
    print(f"'{nombre_contacto}' fue agregado a contactos")


def ver_contactos(lista_contactos):
    if not lista_contactos:
        print("No hay contactos")
        return
    print("\n---- Contactos ----")
    for i, (nombre_contacto, numero_telefono) in enumerate(lista_contactos, start=1): # Usa enumerate(lista_contactos, start=1) para numerarlas desde 1 en vez de 0.
        print(f"{i}. {nombre_contacto} - {numero_telefono}")


def buscar_contacto(lista_contactos):
    nombre_contacto = input("Ingrese el nombre a buscar: ").strip().lower().capitalize()
    for contacto in lista_contactos:
        if contacto[0] == nombre_contacto:
            print(f"Contacto encontrado: {contacto[0]} - {contacto[1]}")
            return
    print("No se encontró el contacto.")


def eliminar_contacto(lista_contactos):
    ver_contactos(lista_contactos)
    nombre_contacto = input("Ingrese el nombre del contacto a eliminar: ").strip().lower().capitalize()
    for contacto in lista_contactos:
        if contacto[0] == nombre_contacto:
            lista_contactos.remove(contacto)
            print(f"Contacto '{nombre_contacto}' eliminado.")
            return
    print("No se encontró el contacto.")


def ejecutar():
    lista_contactos = []
    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregar_contacto(lista_contactos)
            elif opcion == 2:
                ver_contactos(lista_contactos)
            elif opcion == 3:
                buscar_contacto(lista_contactos)
            elif opcion == 4:
                eliminar_contacto(lista_contactos)
            elif opcion == 5:
                print("HASTA PRONTO")
                break
            else:
                print("ERROR: Opción invalida")
        except ValueError:
            print("ERROR: Ingrese un numero valido")


ejecutar()