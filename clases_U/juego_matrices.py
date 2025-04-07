import random

def crear_tablero(fila1, fila2, fila3):
    i = 0
    while i < 3:
        numero_random = random.randint(0, 2)
        fila1 [i] = numero_random
        i += 1
    i = 0
    while i < 3:
        numero_random = random.randint(0, 2)
        fila2 [i] = numero_random
        i += 1
    i = 0
    while i < 3:
        numero_random = random.randint(0, 2)
        fila3 [i] = numero_random
        i += 1


def coordenadas():
     while True:
        try:
            posicion = int(input("Ingrese una posicion (0, 1, 2): "))
            if posicion >= 0:
                return posicion
            else:
                print("ERROR: Ingrese una posicion valida")
        except ValueError:
            print("ERROR: Ingrese un numero")


# def colocar_bomba():
 posicion_columna = int(input("Ingrese columna (0, 1, 2): "))
            if posicion_columna >= 0:
                posicion_fila = int(input("Ingrese fila (0, 1, 2): "))
                if posicion_fila >= 0:
                    posicion = int(input("Ingrese posicion (0, 1, 2): "))
                    return posicion_columna, posicion_fila, posicion

def ejecutar():
    fila1 = []
    fila2 = []
    fila3 = []
    crear_tablero(fila1, fila2, fila3)
    while True:
        print("Ingrese coordenada fila:")
        posicion = coordenadas()
        if posicion == 0:
             print("Ingrese coordenada columna:")
             posicion = coordenadas()
             if posicion == 0:
                  
             
             