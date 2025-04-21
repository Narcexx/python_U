# Escribe una función que tome una matriz como entrada y muestre la matriz resultante de su multiplicación por un escalar.
import random

# Funcion que crea la matriz, recibe como parametros las filas y columnas que tendra la matriz
def crear_matriz(fila, columna):
    matriz = [] # Ss declara una matriz
    for i in range(fila): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(columna): # Este for ira pasando por las columnas, el for terminara cuando se llegue al numero de columnas que dio el usuario
            valor = random.randint(0,6)  # Se crea una variable que guarde numeros randoms entre el 0 y 6
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz # Al finalizar los for, retornara la matriz creada

# Funcion para mostrar la matriz antes de la transpuesta, recibe como parametros las fila, columna que tiene y la matriz
def mostrar_matriz(matriz, fila, columna):
    for i in range(fila):
        for j in range(columna):
            print(matriz[i][j], end=' ') # Aqui va imprimiendo las filas y con el end=' ' no hace el salto de linea y separa los numeros por un espacio
        print()

# Funcion que creara la matriz multiplicada por un escalar, recibe como parametros matriz la cual se le aplicara el escalar, fila, columna, escalar
def matriz_escalar(matriz, fila, columna, escalar):
    matriz_resultado = []
    for i in range(fila): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas que dio el usuario
        fila = [] # Se crea una lista que se llame fila
        for j in range(columna): # Este for ira pasando por las columnas y sumando, el for terminara cuando se llegue al numero de columnas que dio el usuario
            resultado = matriz[i][j] * escalar # Se crea una variable que guarde el resultado de esa coordenada
            fila.append(resultado) # Aqui con el metodo .append() agregara el resultado a la lista fila
        matriz_resultado.append(fila) # Cuando termine el for de las columnas, significa que se hicieron todas las sumas de esa fila, entonces se agrega la lista fila a la matriz_resultado
        # Despues se creara otra fila si es que el usuario puso mas de una y hara el mismo procedimiento
    return matriz_resultado # Al finalizar los for, retornara la matriz_resultado


# Funcion para validar que se ingrese un numero que sea mayor que 0 y que no sea una letra, asi el programa no se detendra si se coloca 0, entero negativo o letra
def validacion_dato(dato):
    while True:
        try:
            numero = int(input(dato))
            if numero > 0:
                return numero # Retorna el numero si se ingreso un numero valido
            else:
                print("Tiene que ser mayo que 0")
        except ValueError:
            print("INGRESE UN NUMERO VALIDO")


def ejecutar():
    fila = validacion_dato("Cuantas fila tendra la matriz: ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
    columna = validacion_dato("Cuantas columnas tendra la matriz: ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto
    escalar = validacion_dato("De el numero para hacer la multiplicacion por un escalar: ") # Se invoca a la funcion validacion_dato(), y se le entrega como argumento en este caso una cadena de texto

    matriz = crear_matriz(fila, columna) # Se invoca a la funcion crear_matriz() para crear la matriz y se les pasa los argumentos de fila y columna
    matriz_resultado = matriz_escalar(matriz, fila, columna, escalar) # Se invoca a la funcion matriz_escalar() para crear una matriz multiplicada por un escalar, se le pasa como argumentos matriz, fila, columna, escalar
    print("La matriz:")
    mostrar_matriz(matriz, fila, columna)
    print(f"La matriz resultante de su multiplicacion por el escalar {escalar}:")
    mostrar_matriz(matriz_resultado, fila, columna)

ejecutar()