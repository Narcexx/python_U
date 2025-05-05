# Crear el juego del busca minas
import random

# Funcion que crea la matriz
def crear_matriz():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(4):
            valor = " "
            fila.append(valor)
        matriz.append(fila)
    return matriz

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

# Funcion para validar que se ingrese un numero que sea mayor que 0, menor que 5 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero > 0 and numero < 5:
                return numero
            else:
                print("Tiene que ser mayor que 0 y menor a 5")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")

# Funcion para crear entre 1 y 4 bombas en posiciones aleatorias sin repetir
def posicion_bomba():
    cantidad = random.randint(1, 3)  # Genera un numero aleatorio entre 1 y 3 bombas
    bombas = []  # Lista para guardar las bombas
    # While que se repitira mientras no se llene hasta la cantidad de bombas
    while len(bombas) < cantidad:
        fila = random.randint(0, 3)  # Elige una fila aleatoria
        columna = random.randint(0, 3)  # Elige una columna aleatoria
        if [fila, columna] not in bombas: # Este if es para que no se coloquen dos bombas en la misma posicion
            bombas.append([fila, columna])  # Agrega esa bomba a la lista
    return bombas  # Devuelve la lista de posiciones ejem [[fila, columna], [fila, columna]]

# Funcion que cuenta cuantas bombas hay alrededor de una posicion
def contar_bombas_alrededor(fila, columna, bombas):
    contador = 0
    # fors que revisa todas las posiciones alrededor
    for i in range(fila - 1, fila + 2):  # Mira la fila anterior y siguiente ejem si fila = 2 entonces esto seria range(1, 3) que va desde el 1 hasta el 3
        for j in range(columna - 1, columna + 2):  # Mira la columna anterior y siguiente ejem si columna = 2 entonces esto seria range(1, 3)
            if [i, j] in bombas and [i, j] != [fila, columna]: # Este if es ver si [i, j] tiene una bomba y que no sea la misma posicion del jugador
                if i >= 0 and i < 4 and j >= 0 and j < 4: # Este if es para verificar que la posicion esta dentro de la matriz 4x4
                    contador += 1  # Sumamos 1 al contador
    return contador  # Retornamos el numero de bombas que hay alrededor

# Funcion que revisa la jugada del jugador
def movimiento_jugador(fila, columna, matriz, bombas):
    if matriz[fila][columna] != " ": # Este if es para ver si ya se jugo la posicion
        print("Ya jugaste en esa posición.")
        return False  # Retorna False para que no cuente esta turno
    if [fila, columna] in bombas: # Este if verifica si la posicion que se jugo este en la lista de bombas
        matriz[fila][columna] = "B"  # Coloca una B de bomba en la matriz
        return "bomba"
    else: # Si no es bomba cuenta las bombas alrededor y las agrega al tablero
        cantidad = contar_bombas_alrededor(fila, columna, bombas) # Invoca a la funcion contar_bombas_alrededor(), con los argumentos fila, columna, bombas. Esto para pasar la cantidad de bombas que hay alrededor
        matriz[fila][columna] = str(cantidad)  # Coloca el numero en la posicion
        return True  # Retorna True entonces el juego seguira

def ejecutar():
    matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear una matriz 4x4
    mostrar_matriz(matriz)
    bombas = posicion_bomba() # Se invoca a la funcion posicion_bomba() que crea entre 1 y 3 bombas en posiciones aleatorias
    total_casillas = 16
    descubiertas = 0

    while True:
        print("Jugador", end=' ')
        fila = validacion_dato("Elige fila (1 a 4): ") - 1
        columna = validacion_dato("Elige columna (1 a 4): ") - 1
        resultado = movimiento_jugador(fila, columna, matriz, bombas) # Se invoca a la movimiento_jugador() que revisa si el jugador descubrio una bomba o una posicion
        if resultado == "bomba": # Si es una bomba se muestra la bomba y se termina el juego
            print("BOOM! Pisaste una bomba!")
            mostrar_matriz(matriz)
            break
        elif resultado == True: #  Si retorna True se suma 1 a las posiciones descubiertas
            descubiertas += 1
        mostrar_matriz(matriz) # Se muestra el tablero ahora con la cantidad de bombas cerca de esa posicion
        # Si ya se descubrieron todas las casillas sin bomba se gana
        if descubiertas == total_casillas - len(bombas):
            print("¡Felicidades! Descubriste todas las casillas sin bombas.")
            break
    # Al final se muestran las posiciones de las bombas
    print("Las bombas estaban en:")
    for f, c in bombas:
        print(f"Fila {f+1}, Columna {c+1}")

ejecutar()