# invasores.py

# Crear tablero 5x5 con invasores en la primera fila
tablero = [["I", "I", "I", "I", "I"],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "]]

# Posición inicial de la nave
pos_nave = 2
tablero[4][pos_nave] = "N"

juego_activo = True

while juego_activo:
    print("\nTablero:")
    i = 0
    while i < 5:
        print(" ".join(tablero[i]))
        i += 1

    accion = input("Mover (a=izquierda, d=derecha) o disparar (w): ")

    if accion == "a" and pos_nave > 0:
        tablero[4][pos_nave] = " "
        pos_nave -= 1
        tablero[4][pos_nave] = "N"
    elif accion == "d" and pos_nave < 4:
        tablero[4][pos_nave] = " "
        pos_nave += 1
        tablero[4][pos_nave] = "N"
    elif accion == "w":
        fila = 3
        while fila >= 0:
            if tablero[fila][pos_nave] == "I":
                tablero[fila][pos_nave] = " "
                print("¡Invasor eliminado!")
                break
            fila -= 1
    else:
        print("Acción inválida.")

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

