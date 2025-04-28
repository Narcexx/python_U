# Crear el juego del gato, que se pueda jugar con alguien o con la maquina
import random

# Funcion que crea la matriz
def crear_matriz():
    matriz = [] # Se declara una matriz
    for i in range(3): # Este for es para ir creando las filas
        fila = [] # Se crea una lista que se llame fila
        for j in range(3): # Este for ira pasando por las columnas
            valor = " "  # Se crea una variable que guarde un string con un espacio para dejar la celda vacia
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila
    return matriz # Al finalizar los for, retornara la matriz creada

# Funcion para mostrar la matriz, recibe como parametro la matriz
def mostrar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j], end=' | ') # Aqui va imprimiendo las filas y con el end=' ' no hace el salto de linea y separa los numeros por un espacio
        print()
        if i == 2:
            print()
        else: 
            print("--|---|--")

# Funcion para validar que se ingrese un numero que sea mayor que 0, menor que 4 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
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

# Funcion para colocar en la matriz el movimiento del jugador, recibe como parametro la fila y columna como la posicion donde jugo, la matriz y el jugador que le toca en ese turno
def movimiento_jugador(fila, columna, matriz, jugador):
    if jugador == 1:     
        simbolo = "O"
    elif jugador == 2:
        simbolo = "X"

    if matriz[fila-1][columna-1] != " ": # Si la posicion que se jugo no esta con un string vacio eso quiere decir que se jugo retornara False
        print("Esa posicion ya se jugo")
        return False  
    else:
        matriz[fila-1][columna-1] = simbolo # Entonce si no entro al if eso quiere decir que la posicion estaba con un string vacio, se cambia por el simbolo que corresponde y retrona True
        return True 
    


def ejecutar():
    matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear una matriz 3x3
    mostrar_matriz(matriz)
    turno = 1
    while turno < 9:
        if turno % 2 == 1:
            jugador = 1
        elif turno % 2 == 0:
            jugador = 2
        while True:
            fila = validacion_dato("Elige fila (1, 2, 3): ")
            columna = validacion_dato("Elige columna (1, 2, 3): ")
            if movimiento_jugador(fila, columna, matriz, jugador): # Si no estaba ocupada la posicion retornara True y se ejecutara el break
                break  
        mostrar_matriz(matriz)
        turno += 1
    
ejecutar()
