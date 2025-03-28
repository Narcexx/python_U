def get_product(**datos):
    print(datos)

get_product(id = "id", name = "Iphone", desc = "Esto es un Iphone") # Cada vez que que se llama una funcion que utilice el kwargs hay que indicar el nombre del parametro


def get_product2(**datos):
    print(datos["id"], datos ["name"])

get_product2(id = "23", name = "Iphone", desc = "Esto es un Iphone")