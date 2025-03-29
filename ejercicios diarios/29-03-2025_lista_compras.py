def menu():
    print("\n---- MENU ----")
    print("1. Agregar producto")
    print("2. Ver lista de compras")
    print("3. Eliminar producto")
    print("4. Salir")


def agregar_producto(productos):
    productos.append(input("Nombre producto: ").lower().capitalize())
    # return productos # ESTA LINEA LA MODIFIQUE POR CONSEJO DE CHATGPT, ya que el return estaba mal


def ver_lista(productos):
    if productos: # ESTA LINEA LA AGRUEGUE POR CONSEJO DE CHATGPT
        for producto in productos:
            print(producto)
    else:
        print("La lista de compras esta vacia") # ESTA LINEA LA AGRUEGUE POR CONSEJO DE CHATGPT


def eliminar_prodcutos_lista(productos):
    producto_eliminar = input("Nombre producto eliminar: ").lower().capitalize()
    if producto_eliminar in productos:
        productos.remove(producto_eliminar)
        # return productos
        print(f"'{producto_eliminar}' eliminado de la lista.") # ESTA LINEA LA AGRUEGUE POR CONSEJO DE CHATGPT, ya que el return estaba mal
    else:
        # return "No esta el producto en la lista" 
        print("El producto no está en la lista.") # ESTA LINEA LA AGRUEGUE POR CONSEJO DE CHATGPT, ya que el return estaba mal


def ejecutar():
    productos = []
    while True:
        menu()
        try:
            op = int(input("Que desea hacer?: "))
            if op == 4:
                print("\nHASTA LUEGO\n")
                break
            elif op == 1:
                agregar_producto(productos)
            elif op == 2:
                ver_lista(productos)
            elif op == 3:
                eliminar_prodcutos_lista(productos)
            else:
                print("ERROR: Elija opcion valida")
        except ValueError:
            print("ERROR: Ingrese una opcion numerica")


ejecutar()