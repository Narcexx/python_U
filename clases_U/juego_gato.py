# Crear el juego del gato, que se pueda jugar con alguien o con la maquina
import random

# Funcion que crea la matriz, recibe como parametros las filas y columnas que tendra la matriz
def crear_matriz():
    matriz = [] # Ss declara una matriz
    for i in range(3): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(3): # Este for ira pasando por las columnas, el for terminara cuando se llegue al numero de columnas que dio el usuario
            valor = " "  # Se crea una variable que guarde un string con un espacio para dejar la celda vacia
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz # Al finalizar los for, retornara la matriz creada

# Funcion para mostrar la matriz antes de la transpuesta, recibe como parametros las fila, columna que tiene y la matriz
def mostrar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            if True in [matriz[0][2], matriz[1][2], matriz[2][2]]:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j], end=' | ') # Aqui va imprimiendo las filas y con el end=' ' no hace el salto de linea y separa los numeros por un espacio
        print()
        if i == 2:
            print()
        else: 
            print("--|---|--")

# Funcion para validar que se ingrese un numero que sea mayor que 0 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero > 0 and numero < 4:
                return numero # Retorna el numero si se ingreso un numero valido
            else:
                print("Tiene que ser mayor que 0 o menor a 4")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")


def movimiento_jugador(fila, columna, matriz, jugador):
    if jugador == 1:     
        simbolo = "O"
    elif jugador == 2:
        simbolo = "X"

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == "O" or matriz[i][j] == "X":
                print("Se jugo esa posicion ya")
            elif matriz[fila-1][columna-1] == " ":
                matriz [fila-1][columna-1] = simbolo
            
    


def ejecutar():
    matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear la matriz y se les pasa los argumentos de fila y columna
    mostrar_matriz(matriz)
    turno = 1
    while turno < 5:
        if turno % 2 == 1:
            jugador = 1
        elif turno % 2 == 0:
            jugador = 2
        fila = validacion_dato("Elige fila (1, 2, 3): ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
        columna = validacion_dato("Elige columna (1, 2, 3): ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
        movimiento_jugador(fila, columna, matriz, jugador)
        mostrar_matriz(matriz)
        turno += 1
    
ejecutar()
