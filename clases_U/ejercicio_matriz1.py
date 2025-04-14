import random

def crear_matriz(fila, columna):
    matriz = []
    for i in range(fila):
        fila = []
        for j in range(columna):
            valor = random.randint(3,6)
            fila.append(valor)
        matriz.append(fila)
    return matriz


def suma_matriz(fila, columna, matriz1, matriz2):
    matriz3 = []
    for i in range(fila):
        fila = []
        for j in range(columna):
            resultado = matriz1[i][j] + matriz2[i][j]
            fila.append(resultado)
        matriz3.append(fila)

    return matriz3


def ejecutar():
    fila = int((input("Cuantas fila tendra la matriz: ")))
    columna = int(input("Cuantas columnas tendra la matriz: "))
    matriz1 = crear_matriz(fila, columna)
    matriz2 = crear_matriz(fila, columna)
    matriz3 = suma_matriz(fila, columna, matriz1, matriz2)
    print(f"Matriz 1: {matriz1}")
    print(f"Matriz 2: {matriz2}")
    print(f"La matriz resultante es: {matriz3}")

ejecutar()

# def crear_matriz2():
#     fila = int((input("Cuantas fila tendra la matriz: ")))
#     columna = int(input("Cuantas columnas tendra la matriz: "))
#     matriz = []
#     return [[random.randint(0,4) for j in range(columna)]for i in range(fila)]
# print(crear_matriz2())