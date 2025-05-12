# invasores.py

# Crear matriz 5x5 con invasores en la primera fila
def crear_matriz():
    tablero =   [["I", "I", "I", "I", "I"],
                 [" ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " "]]
    return tablero


def mostrar_juego(tablero):
    i = 0
    while i < 5:
        print(" ".join(tablero[i]))
        i += 1


def movimiento_nave(tablero, pos_nave, accion):
    tablero[4][pos_nave] = " "
    if accion == "a" and pos_nave > 0:
        pos_nave -= 1
    elif accion == "d" and pos_nave < 4:
        pos_nave += 1
    tablero[4][pos_nave] = "N"
    return pos_nave


def disparo(tablero, pos_nave, accion):
    if accion == "w":
        fila = 3
        while fila >= 0:
            if tablero[fila][pos_nave] == "I":
                tablero[fila][pos_nave] = " "
                print("¡Invasor eliminado!")
                break
            fila -= 1
    else:
        print("Acción inválida.")

def verificar_invasores(tablero):
    # Verificar si hay invasores
    fila_check = 0
    invasores_quedan = False
    while fila_check < 5:
        columna_check = 0
        while columna_check < 5:
            if tablero[fila_check][columna_check] == "I":
                invasores_quedan = True
            columna_check += 1
        fila_check += 1

    if not invasores_quedan:
        juego_activo = False
        print("\n¡Has eliminado a todos los invasores!")

# Posición inicial de la nave
# pos_nave = 2
# tablero[4][pos_nave] = "N"

# juego_activo = True

# accion = input("Mover (a=izquierda, d=derecha) o disparar (w): ")

#     # Verificar si hay invasores
#     fila_check = 0
#     invasores_quedan = False
#     while fila_check < 5:
#         columna_check = 0
#         while columna_check < 5:
#             if tablero[fila_check][columna_check] == "I":
#                 invasores_quedan = True
#             columna_check += 1
#         fila_check += 1

#     if not invasores_quedan:
#         juego_activo = False
#         print("\n¡Has eliminado a todos los invasores!")

tablero = crear_matriz()
# Posición inicial de la nave
pos_nave = 2
tablero[4][pos_nave] = "N"
mostrar_juego(tablero)
accion = input("Mover (a=izquierda, d=derecha) o disparar (w): ")
movimiento_nave(tablero, pos_nave, accion)