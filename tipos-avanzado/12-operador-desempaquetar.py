lista = [1, 2, 3, 4]
tupla = (5, 6, 7, 8)
print(1, 2, 3, 4)
print(*lista) # No los imprime como lista
print(*tupla)

lista2 = [5, 6]
combinada = [0, *lista, "xd", *lista2, 7]
print(combinada)


punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1,"lala": 30, **punto2, "z": "mundo"} # Hace la asignacion de porpiedades de derecha a izquierda
print(nuevoPunto)