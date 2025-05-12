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
            if numero >= 0 and numero < 5:
                return numero
            else:
                print("Coordenadas fuera de rango.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

# Colocar 3 tesoros en posiciones aleatorias
def tesoros_posiciones(tablero):
    tesoros_restantes = 3
    while tesoros_restantes > 0:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "T"
            tesoros_restantes -= 1

# Matriz para mostrar al jugador (sin mostrar los tesoros)
def tablero_no_tesoros():
    jugador_tablero = [["-" for j in range(8)] for i in range(8)]
    return jugador_tablero

def ejecutar():
    encontrados = 0
    tablero = crear_matriz()
    jugador_tablero = tablero_no_tesoros()
    tesoros_posiciones(tablero)
    intentos = 0

    while encontrados < 3:
        print("\nMapa:")
        i = 0
        while i < 8:
            print(" ".join(jugador_tablero[i]))
            i += 1

        fila = validacion_dato("Ingrese fila (0-4): ")
        columna = validacion_dato("Ingrese columna (0-4): ")

        if jugador_tablero[fila][columna] != "-":
            print("Ya buscaste ahí.")
            continue

        if tablero[fila][columna] == "T":
            print("¡Tesoro encontrado!")
            jugador_tablero[fila][columna] = "💰"
            encontrados += 1
        else:
            print("Nada por aquí...")
            jugador_tablero[fila][columna] = "X"
        
        if encontrados == 3:
            print("\n¡Has encontrado todos los tesoros!")
        
        intentos += 1
        if intentos == 10:
            break
ejecutar()
