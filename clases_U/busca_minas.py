# Crear el juego del busca minas
import random

# Funcion que crea la matriz
def crear_matriz():
    matriz = [] # Se declara una matriz
    for i in range(4): # Este for es para ir creando las filas
        fila = [] # Se crea una lista que se llame fila
        for j in range(4): # Este for ira pasando por las columnas
            valor = " "  # Se crea una variable que guarde un string con un espacio para dejar la celda vacia
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila
    return matriz # Al finalizar los for, retornara la matriz creada

# Funcion para mostrar la matriz, recibe como parametro la matriz
def mostrar_matriz(matriz):
    for i in range(4):
        for j in range(4):
            if j == 3:
                print(matriz[i][j], end=' ') # Aqui cuando este en la columna final de cada fila terminara con espacio en blanco
            else:
                print(matriz[i][j], end=' | ') # Aqui va imprimiendo las filas y con el end=' | ' despues de cada posicion
        print()
        if i == 3:
            print()
        else: 
            print("--|---|---|--") # Imprime esto abajo de cada fila menos de la ultima

# Funcion para validar que se ingrese un numero que sea mayor que 0, menor que 4 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero > 0 and numero < 4:
                return numero # Retorna el numero si se ingreso un numero valido
            else:
                print("Tiene que ser mayor que 0 y menor a 4")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")

# Funcion para darle una posicion random en la matriz a la bomba o bombas
def posicion_bomba():
    fila = random.randint(1, 3)
    columna = random.randint(1, 3)
    return fila, columna


# Funcion para colocar en la matriz el movimiento del jugador, recibe como parametro la fila y columna como la posicion donde jugo, la matriz y el jugador que le toca en ese turno
def movimiento_jugador(fila, columna, matriz):
    if matriz[fila][columna] != " ": # Si la posicion que se jugo no esta vacia
        print("Esa posicion ya se jugo\n")
        return False
    # Contar las bombas cercanas
    cant_bombas = 0
    for i in range(fila - 1, fila + 2):  # Recorrer las filas adyacentes
        for j in range(columna - 1, columna + 2):  # Recorrer las columnas adyacentes
            if 0 <= i < 4 and 0 <= j < 4:  # Asegurarse de que las coordenadas estén dentro de la matriz
                if matriz[i][j] == "B":
                    cant_bombas += 1
    matriz[fila][columna] = str(cant_bombas)  # Coloca el numero de bombas en la casilla seleccionada
    return True

# Funcion para verificar si el jugador ha ganado
def revisar_ganador(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == " ":
                return False  # Si hay alguna celda vacía, el jugador no ha ganado
    return True  # Si no quedan celdas vacías, el jugador ha ganado

def ejecutar():
    matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear una matriz 4x4
    bomba_fila, bomba_columna = posicion_bomba() # Genera una bomba aleatoria
    matriz[bomba_fila][bomba_columna] = "B"  # Coloca la bomba en la matriz
    turno = 1
    mostrar_matriz(matriz)
    
    while turno <= 16:
        print(f"Turno del Jugador {turno}")
        # Turno jugador
        while True:
            fila = validacion_dato("Elige fila (1, 2, 3): ") - 1  # Restar 1 para ajustarse al índice 0-based
            columna = validacion_dato("Elige columna (1, 2, 3): ") - 1
            if movimiento_jugador(fila, columna, matriz): # Si no estaba ocupada la posicion y no hay bomba
                break
        mostrar_matriz(matriz)  # Se muestra la matriz con el movimiento del jugador
        
        if revisar_ganador(matriz):
            print(f"Jugador {turno} GANÓ!")
            break
        
        turno += 1  # Si no ha ganado, se pasa al siguiente turno

ejecutar()

# matriz = crear_matriz()
# mostrar_matriz(matriz)