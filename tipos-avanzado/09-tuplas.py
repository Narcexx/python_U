# LAS TUPLAS SON LO MISMO QUE UNA LISTA SOLO QUE LAS TUPLAS NO SE PUEDEN MODIFICAR NO SE PUEDEN AGREGAR, NI QUITAR ELEMENTOS
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2]) # Transformar una lista en una tupla
print(punto)

# A las tuplas se le puede hacer todas las cosas que puedes hacer con las listas, menos modificarla
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# En caso de querer modificar una tupla, pero esto nunca deberia pasar se hace asi
listaNumeros = list(numeros)
listaNumeros[0] = "xd"
print(listaNumeros)
