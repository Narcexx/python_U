# caza_tesoro.py
import random

# Crear matriz 5x5 vacía
def crear_matriz():
    tablero = []
    i = 0
    while i < 8:
        j = 0
        fila = []
        while j < 8:
            fila.append(" ")
            j += 1
        tablero.append(fila)
        i += 1

    return tablero

# Funcion para validar que se ingrese un numero que sea mayor que 0, menor que 5 y que no sea una letra, asi el programa no se detendra si se coloca 0, numero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero >= 0 and numero < 8:
                return numero
            else:
                print("Coordenadas fuera de rango.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

# Colocar 3 tesoros en posiciones aleatorias
def tesoros_posiciones(tablero):
    tesoros_restantes = 3
    while tesoros_restantes > 0:
        fila = random.randint(0, 7)
        columna = random.randint(0, 7)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "T"
            tesoros_restantes -= 1

# Matriz para mostrar al jugador (sin mostrar los tesoros)
def tablero_no_tesoros():
    return [[" - " for _ in range(8)] for _ in range(8)]

# Mostrar el tablero del jugador
def mostrar_tablero(tablero):
    print("\nMapa:")
    i = 0
    while i < 8:
        print(" ".join(tablero[i]))
        i += 1


def mostrar_tablero_real(tablero):
    print("\nTablero real:")
    i = 0
    while i < 8:
        fila = []
        j = 0
        while j < 8:
            if tablero[i][j] == "T":  # Mostrar "T" solo si es un tesoro
                fila.append(" T ")
            else:
                fila.append(" - ")  # Mostrar guion si no es un tesoro
            j += 1
        print(" ".join(fila))
        i += 1

# Contar tesoros en fila y columna
def pista_tesoros(tablero, jugador_tablero, fila, columna):
    tesoros_fila = 0
    tesoros_columna = 0

    for i in range(8):
        if tablero[fila][i] == "T" and jugador_tablero[fila][i] == " - ":
            tesoros_fila += 1
        if tablero[i][columna] == "T" and jugador_tablero[i][columna] == " - ":
            tesoros_columna += 1

    return tesoros_fila, tesoros_columna


def ejecutar():
    encontrados = 0
    tablero = crear_matriz()
    jugador_tablero = tablero_no_tesoros()
    tesoros_posiciones(tablero)
    intentos = 15

    while encontrados < 3 and intentos > 0:
        mostrar_tablero(jugador_tablero)

        fila = validacion_dato("Ingrese fila (0-7): ")
        columna = validacion_dato("Ingrese columna (0-7): ")

        if jugador_tablero[fila][columna] != " - ":
            print("Ya buscaste ahí.")
            continue

        if tablero[fila][columna] == "T":
            print("¡Tesoro encontrado!")
            jugador_tablero[fila][columna] = "💰 "
            encontrados += 1
        else:
            print("Nada por aquí...")
            jugador_tablero[fila][columna] = " X "

        # Mostrar cuantos tesoros quedan
        print("Tesoros restantes:", 3 - encontrados)

        # Mostrar pistas
        tesoros_fila, tesoros_columna = pista_tesoros(tablero, jugador_tablero, fila, columna)
        print(f"Pista: hay {tesoros_fila} tesoro(s) en la misma fila y {tesoros_columna} en la misma columna")
        intentos -= 1
        print(f"Te quedan {intentos} intentos")

    if encontrados == 3:
        print("\n¡Has encontrado todos los tesoros!")
    else:
        print("\nSe acabaron los intentos")
        mostrar_tablero_real(tablero)


ejecutar()
