# Implementa una función que tome una matriz como entrada y muestre la matriz transpuesta.
import random

# Funcion que crea la matriz, recibe como parametros las filas y columnas que tendra la matriz
def crear_matriz(fila, columna):
    matriz = [] # Ss declara una matriz
    for i in range(fila): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(columna): # Este for ira pasando por las columnas, el for terminara cuando se llegue al numero de columnas que dio el usuario
            valor = random.randint(0,6)  # Se crea una variable que guarde numeros randoms entre el 0 y 6
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz # Al finalizar los for, retornara la matriz creada

# Funcion para mostrar la matriz antes de la transpuesta, recibe como parametros las fila, columna que tiene y la matriz
def mostrar_matriz(fila, columna, matriz):
    for i in range(fila):
        for j in range(columna):
            print(matriz[i][j], end=' ') # Aqui va imprimiendo las filas y con el end=' ' no hace el salto de linea y separa los numeros por un espacio
        print()

# Otra forma de hacerlo, mas compacta
# def mostrar_matriz(matriz):
#     for fila in matriz: # Aca recorrera la matriz. ejem la matriz es [[3, 2, 3],[6, 1, 2]] entonces entrara a la primera fila que es [3, 2, 3]
#         for valor in fila: # Aca recorrera la fila [3, 2, 3]
#             print(valor, end=' ') # Mostrara los valores de la fila en una linea
#         print()
        # Terminado el for pasara al siguiente fila que es [6, 1, 2] y ahara lo mismo


# Funcion para mostrar la matriz transpuesta, recibe como parametros las fila, columna que tiene y la matriz
def mostrar_matriz_transpuesta(fila, columna, matriz):
    # Se intercambia el orden ahora van primero las columnas despues las filas, ya que eso es la transpuesta de una matriz
    # Entonces si se le da una matriz 2(filas)x3(columnas) la transpuesta de esta matriz seria 3(filas)x2(columnas)
    # Los valores de la fila deberian imprimirse hacia abajo en columna
    for j in range(columna):
        for i in range(fila):
            print(matriz[i][j], end=' ') 
        print()


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

    matriz = crear_matriz(fila, columna) # Se invoca a la funcion crear_matriz() para crear la matriz y se les pasa los argumentos de fila y columna
    mostrar_matriz(fila, columna, matriz)
    print()
    mostrar_matriz_transpuesta(fila, columna, matriz)

ejecutar()
    