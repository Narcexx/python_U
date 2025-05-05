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
                print(matriz[i][j], end=' ') # Aqui cuando este en la columna final de cada fila terminara con espacio en blanco
            else:
                print(matriz[i][j], end=' | ') # Aqui va imprimiendo las filas y con el end=' | ' despues de cada posicion
        print()
        if i == 2:
            print()
        else: 
            print("--|---|--") # Imprime esto abajo de cada fila menos de la ultima

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

# Funcion para colocar en la matriz el movimiento del jugador, recibe como parametro la fila y columna como la posicion donde jugo, la matriz y el jugador que le toca en ese turno
def movimiento_jugador(fila, columna, matriz, jugador):
    if jugador == 1:     
        simbolo = "O"
    elif jugador == 2:
        simbolo = "X"

    if matriz[fila-1][columna-1] != " ": # Si la posicion que se jugo no esta con un string vacio eso quiere decir que se jugo retornara False
        print("Esa posicion ya se jugo\n")
        return False  
    else:
        matriz[fila-1][columna-1] = simbolo # Entonce si no entro al if eso quiere decir que la posicion estaba con un string vacio, se cambia por el simbolo que corresponde y retrona True
        return True 
    
# Funcion que revisa despues de cada movimiento si hay ganador o no, recibe como parametro la matriz
def revisar_ganador(matriz):
    # Revisa filas y columnas
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != " ":
            return True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            return True
    # Revisa diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " ":
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        return True
    
    return False

# Funcion para el movimiento de la maquina full random
# def movimiento_pc(matriz):
#     while True:
#         fila = random.randint(0, 2)
#         columna = random.randint(0, 2)
#         if(matriz[fila][columna] == " "): # Si no hay nada va a poner el simbolo en la posicion
#             matriz[fila][columna]="X"
#             break
#         else: # Si estaba con algo esa posicion, va pasar a al continue que repetira el bucle y se creara otra posicion para comparar
#             continue

# Funcion para el movimiento de la maquina pero mas inteligente
def movimiento_pc(matriz):
    # Este for es va a verificar que si con este movimiento gana o no
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == " ":
                matriz[i][j] = "X"  # Simula que pone su ficha
                if revisar_ganador(matriz): # Si gana con este movimiento lo retornara
                    return
                matriz[i][j] = " "  # Si no gana vuelve a colocar el string vacio
    # Este for se ejecutara si el for de arriba no retorno, este es para ver si bloquea la jugada ganadora del jugador
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == " ":
                matriz[i][j] = "O"  # Simula que el jugador pone su ficha
                if revisar_ganador(matriz): # Si gana con ese movimiento el jugador lo va a bloquear
                    matriz[i][j] = "X"  # Bloquea
                    return
                matriz[i][j] = " "  # # Si no gana el jugador vuelve a colocar el string vacio
    # Si no puede ganar ni bloquear va hacer un movimiento full random
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if matriz[fila][columna] == " ":
            matriz[fila][columna] = "X"
            break
        
# ESTE ES PARA JUGAR CON OTRA PERSONA
# def ejecutar():
#     matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear una matriz 3x3
#     mostrar_matriz(matriz)
#     turno = 1
#     while turno <= 9:
#         # Este bloque if-elif es para identificar saber que jugador le toca en cada turno, turno impar = jugador 1, turno par = jugador 2
#         if turno % 2 == 1:
#             jugador = 1
#         elif turno % 2 == 0:
#             jugador = 2
#         # while para ver si la posicion esta ocupada o no
#         while True:
#             print(f"Jugador {jugador}", end= ' ')
#             fila = validacion_dato("Elige fila (1, 2, 3): ")
#             columna = validacion_dato("Elige columna (1, 2, 3): ")
#             if movimiento_jugador(fila, columna, matriz, jugador): # Si no estaba ocupada la posicion retornara True y se ejecutara el break
#                 break

#         mostrar_matriz(matriz)
        # Invoca la funcion revisar_ganador(), se le pasa como argumento la matriz
#         if revisar_ganador(matriz):
#             print(f"Jugador {jugador} GANO!")
#             break
        # Si despues de el turno del jugador no encuentra ganador suma 1 a la variable turno
        # turno += 1
        # if turno == 10:
        #     print("EMPATE!")

# ESTE ES PARA JUGAR CON LA MAQUINA
def ejecutar():
    matriz = crear_matriz()
    mostrar_matriz(matriz)
    turno = 1
    while turno <= 9:
        # Turno jugador
        # while para ver si la posicion esta ocupada o no
        while True:
            print(f"Jugador 1", end=' ')
            fila = validacion_dato("Elige fila (1, 2, 3): ")
            columna = validacion_dato("Elige columna (1, 2, 3): ")
            if movimiento_jugador(fila, columna, matriz, 1): # Si no estaba ocupada la posicion retornara True y se ejecutara el break
                break
        mostrar_matriz(matriz) # Se muestra la matriz con el movimiento del jugador
        # Invoca la funcion revisar_ganador(), se le pasa como argumento la matriz
        if revisar_ganador(matriz):
            print("Jugador 1 GANO!")
            break
        # Si despues de el turno del jugador no encuentra ganador suma 1 a la variable turno
        turno += 1 
        if turno > 9: # Si turno es igual a 10 significa que se usaron todas las posiciones, entonces es empate
            print("¡EMPATE!")
            break

        # Turno pc
        print("TURNO PC\n")
        movimiento_pc(matriz) # Invoca a la funcion movimiento pc que se le pasa como argumento la matriz
        mostrar_matriz(matriz) # Se muestra la matriz con el movimiento del PC
        # Invoca la funcion revisar_ganador(), se le pasa como argumento la matriz
        if revisar_ganador(matriz):
            print("EL PC GANO!")
            break
        # Si despues de el turno del PC no encuentra ganador suma 1 a la variable turno
        turno += 1
    
ejecutar()
