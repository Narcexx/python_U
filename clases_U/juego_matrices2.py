import random

def crear_tablero():
     fila1 = ["*","*","*"]
     fila2 = ["*","*","*"]
     fila3 = ["*","*","*"]
     return fila1, fila2, fila3


def coordenadas():
     while True:
        try:
            posicion = int(input("Ingrese una posicion (0, 1, 2): "))
            if posicion >= 0 and posicion < 3:
                return posicion
            else:
                print("ERROR: Ingrese una posicion valida")
        except ValueError:
            print("ERROR: Ingrese un numero")


def colocar_bomba():
    fila = random.randint(0, 2)
    columna = random.randint(0, 2)
    return fila, columna


def mostrar(tabla):
    print(tabla [0][0], tabla [0][1], tabla [0][2])
    print(tabla [1][0], tabla [1][1], tabla [1][2])
    print(tabla [2][0], tabla [2][1], tabla [2][2])


def ejecutar():
    tabla = crear_tablero()
    fila_mina, columna_mina = colocar_bomba()
    while True:
        print("---- Tablero ----")
        mostrar(tabla)
        print("Ingrese coordenada de la fila: ")
        posicion_fila = coordenadas()
        print("Ingrese coordenada columna: ")
        posicion_columna = coordenadas()
        if columna_mina == posicion_columna and fila_mina == posicion_fila:
            print("\n¡Boom! Perdiste")
            break
        else:
            print("\nVas bien")
            tabla [posicion_fila][posicion_columna] = "o"

ejecutar()