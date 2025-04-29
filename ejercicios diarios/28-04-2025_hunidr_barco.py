# Crear un juego de hundir el barco, si se pilla el barco en la matriz 3x3 gana
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
                print("Tiene que ser mayor que 0 o menor a 4")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")

# Funcion para colocar en la matriz el movimiento del jugador y verificar si esta el barco en esa posicion, recibe como parametros la fila y columna que dio el jugador, la matriz y la fila y columna del barco
def movimiento_jugador(fila, columna, matriz, barco_fila, barco_columna):

    if fila == barco_fila and columna == barco_columna: # Si la fila y columna que dio el jugador son igual a la posicion donde esta el barco, retoranara True y con la posicion en la matriz con una B de barco
        matriz[fila-1][columna-1] = "B"
        return True 
    else:
        matriz[fila-1][columna-1] = "A" # Y si no concidieron la posicion que dio el jugador con la posicion del barco, en la posicion dada por el jugador se colocara una A que significa que hay agua y retornara False
        return False

# Funcion para darle una posicion random en la matriz al barco
def posicion_barco():
    fila = random.randint(1, 3)
    columna = random.randint(1, 3)
    return fila, columna


def ejecutar():
    matriz = crear_matriz() # Se invoca a la funcion crear_matriz() para crear una matriz 3x3
    barco_fila, barco_columna = posicion_barco()
    intento = 5
    while intento > 0:
        print(f"\nTienes {intento} intentos restantes")
        mostrar_matriz(matriz)
        fila = validacion_dato("Elige fila (1, 2, 3): ")
        columna = validacion_dato("Elige columna (1, 2, 3): ")
        if movimiento_jugador(fila, columna, matriz, barco_fila, barco_columna): # Si estaba el barco en la posicion que dio el jugador retornara True y se ejecutara el break
            print("\nGANASTE! Encontraste el barco\n")
            mostrar_matriz(matriz)
            break
        else: # Si no perderas un intento
            print("\nAGUA\n")
            intento -= 1
    # Si intento llega 0 perdio el jugador, se le dira tambien donde estaba el barco y mostrara la matriz
    if intento == 0:
        print("\nPERDISTE Se acabaron los intentos")
        print(f"El barco estaba en la fila {barco_fila}, columna {barco_columna}")
        matriz[barco_fila-1][barco_columna-1] = "B"
        mostrar_matriz(matriz)

ejecutar()