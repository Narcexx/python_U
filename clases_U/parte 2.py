import os
import time

def crear_tablero():
    tablero = [["I" for _ in range(5)]]
    for _ in range(3):
        tablero.append([" " for _ in range(5)])
    tablero.append([" " for _ in range(5)])  # Fila 4: nave
    return tablero

def mostrar_tablero(tablero, disparo_fila=None, disparo_col=None):
    for i in range(5):
        fila_mostrar = []
        for j in range(5):
            if i == disparo_fila and j == disparo_col:
                fila_mostrar.append("|")
            else:
                fila_mostrar.append(tablero[i][j])
        print(" ".join(fila_mostrar))
    print()

def mover_nave(tablero, pos_nave, direccion):
    tablero[4][pos_nave] = " "
    if direccion == "a" and pos_nave > 0:
        pos_nave -= 1
    elif direccion == "d" and pos_nave < 4:
        pos_nave += 1
    tablero[4][pos_nave] = "N"
    return pos_nave

def disparar(tablero, pos_nave):
    for fila in range(3, -1, -1):
        mostrar_tablero(tablero, disparo_fila=fila, disparo_col=pos_nave)
        time.sleep(0.1)
        if tablero[fila][pos_nave] == "I":
            tablero[fila][pos_nave] = " "
            print("🎯 ¡Invasor eliminado!")
            return True
    print("💨 El disparo no impactó a ningún invasor.")
    return False

def hay_invasores(tablero):
    for fila in tablero:
        if "I" in fila:
            return True
    return False

def mover_invasores(tablero, pos_nave):
    # Verificar si algún invasor bajará sobre la nave
    for col in range(5):
        if tablero[3][col] == "I" and col == pos_nave:
            return True  # Invasor llega a la nave

    # Mover invasores hacia abajo
    for i in range(3, 0, -1):
        tablero[i] = tablero[i - 1][:]
    tablero[0] = [" " for _ in range(5)]
    return False

# Juego principal
def jugar():
    tablero = crear_tablero()
    pos_nave = 2
    tablero[4][pos_nave] = "N"

    juego_activo = True
    turno = 0
    disparos_restantes = 10

    while juego_activo:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia pantalla
        print(f"Disparos restantes: {disparos_restantes}")
        mostrar_tablero(tablero)

        accion = input("Mover (a=izquierda, d=derecha) o disparar (w): ")

        if accion == "a" or accion == "d":
            pos_nave = mover_nave(tablero, pos_nave, accion)
        elif accion == "w":
            if disparos_restantes > 0:
                disparos_restantes -= 1
                disparar(tablero, pos_nave)
            else:
                print("🚫 Ya no te quedan disparos.")
        else:
            print("Acción inválida.")
            continue

        turno += 1

        # Invasores se mueven cada 2 turnos
        if turno % 2 == 0:
            if mover_invasores(tablero, pos_nave):
                mostrar_tablero(tablero)
                print("💥 ¡Un invasor alcanzó tu nave!")
                print("❌ ¡Perdiste!")
                break

        if not hay_invasores(tablero):
            print("🏆 ¡Has eliminado a todos los invasores!")
            break
        elif disparos_restantes == 0 and hay_invasores(tablero):
            print("😓 Se acabaron tus disparos y aún quedan invasores.")
            print("❌ ¡Perdiste!")
            break


jugar()
