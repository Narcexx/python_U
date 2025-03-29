usuarios = [[6, "xdd"], [2, "lol"], [4, "wtf"]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# map
# lista = [expresion for item in items]
# nombres = [usuario[1] for usuario in usuarios] # Esta es una manera mas elegante de hacerlo, para hacer una nueva lista con los elementos seleccionados
# print(nombres)
 
# filter
# nombres = [usuario for usuario in usuarios if usuario[0] > 2] # Estos es para filtar elementos de una lista
# print(nombres)

# nombres = [usuario[1] for usuario in usuarios if usuario[0] > 2] # Aca se combinan las 2 la transformacion y la de filtrar
# print(nombres)

# Esta es otra forma de hacerlo y haciendo un paso primero que el otro con map y filtrer, el anterior era con compresion de listas, las dos maneras estan correctas
nombres = list(map(lambda usuario: usuario[1], usuarios))
print(nombres)
menosUsuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menosUsuarios)