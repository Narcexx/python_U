import random

# Funcion que crea la matriz, recibe como parametros las filas y columnas que tendra la matriz
def crear_matriz(fila, columna):
    matriz = [] # Ss declara una matriz
    for i in range(fila): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(columna): # Este for ira pasando por las columnas, el for terminara cuando se llegue al numero de columnas que dio el usuario
            valor = random.randint(3,6)  # Se crea una variable que guarde numeros randoms entre el 3 y 6
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz # Al finalizar los for, retornara la matriz creada


# Funcion que sumara las matrices en este caso solo son 2 matrices, recibe como parametro la cantidad de filas y columnas y tambien la matriz 1 y la matriz 2
def suma_matriz(fila, columna, matriz1, matriz2):
    matriz3 = [] # Se declara la matriz 3
    for i in range(fila): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(columna): # Este for ira pasando por las columnas y sumando, el for terminara cuando se llegue al numero de columnas que dio el usuario
            resultado = matriz1[i][j] + matriz2[i][j] # Se crea una variable que guarde el resultado de esa coordenada
            fila.append(resultado) # Aqui con el metodo .append() agregara el resultado a la lista fila
        matriz3.append(fila) # Cuando termine el for de las columnas, significa que se hicieron todas las sumas de esa fila, entonces se agrega la lista fila a la matriz 3
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz3 # Al finalizar los for, retornara la matriz 3

# Funcion para validar que se ingrese un numero que sea mayor que 0 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero > 0:
                return numero # Retorna el numero si se ingreso un numero valido
            else:
                print("Tiene que ser mayo que 0")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")


def ejecutar():
    fila = validacion_dato("Cuantas fila tendra la matriz: ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
    columna = validacion_dato("Cuantas columnas tendra la matriz: ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
    
    matriz1 = crear_matriz(fila, columna) # Se invoca a la funcion crear_matriz() para crear la primera matriz y se les pasa los argumentos de fila y columna
    matriz2 = crear_matriz(fila, columna) # Se invoca a la funcion crear_matriz() para crear la segunda matriz y se les pasa los argumentos de fila y columna
    # En este codigo las 2 matrices seran del mismo tamaño
    matriz3 = suma_matriz(fila, columna, matriz1, matriz2) # Se invoca a la funcion suma_matriz(), para crear la matriz que tenga las sumas de cada coordenada, se le pasa los argumentos correspondientes
    print(f"Matriz 1: {matriz1}") 
    print(f"Matriz 2: {matriz2}")
    print(f"La matriz resultante es: {matriz3}")

ejecutar()

# def crear_matriz2():
#     fila = int((input("Cuantas fila tendra la matriz: ")))
#     columna = int(input("Cuantas columnas tendra la matriz: "))
#     matriz = []
#     return [[random.randint(0,4) for j in range(columna)]for i in range(fila)]
# print(crear_matriz2())