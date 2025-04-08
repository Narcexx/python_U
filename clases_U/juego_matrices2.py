import random
# Funcion que crea la matriz
def crear_tablero():
     fila1 = ["*","*","*"]
     fila2 = ["*","*","*"]
     fila3 = ["*","*","*"]
     return [fila1, fila2, fila3]

# Funcion que le pide al usuario que de una posicion retornando esta, se ocupara para pedir posicion de fila y columna
def coordenadas():
     while True:
        try:
            posicion = int(input("Ingrese una posicion (0, 1, 2): "))
            if 0 <= posicion < 3:
                return posicion
            else:
                print("ERROR: Ingrese una posicion valida")
        except ValueError:
            print("ERROR: Ingrese un numero")

# Funcion que pasara las coordenadas randoms de donde estara la bomba
def colocar_bomba():
    fila = random.randint(0, 2)
    columna = random.randint(0, 2)
    return fila, columna

# Funcion que muestra la matriz
def mostrar(tabla):
    print(tabla [0][0], tabla [0][1], tabla [0][2])
    print(tabla [1][0], tabla [1][1], tabla [1][2])
    print(tabla [2][0], tabla [2][1], tabla [2][2])

# Funcion que verifica si una coordenada fue usada
def verificar_coordenada_repetida(posicion_fila, posicion_columna, fila_usada, columna_usada):
    i = 0
    # Entra al bucle mientras i sea menor al tamaño de la lista fila_usada (igual se podia ocupar columna_usada)
    while i < len(fila_usada):
        if fila_usada[i] == posicion_fila and columna_usada[i] == posicion_columna:
            return True
            # Ejemplo de como retorna True
            # fila_usada tiene estos datos [1,0,2] y columna_usada tiene [1,2,1]
            # El usuario pone fila = 0 y columna = 2 entonces cuando i = 1 encontraria la concidencia y retornaria True
        i += 1
    return False


def ejecutar():
    tabla = crear_tablero()
    fila_bomba, columna_bomba = colocar_bomba() # Se invoca a la funcion para guardar las coordenadas donde estara la bomba
    intento = 1
    celdas_correctas = 1
    fila_usada = [] # En esta lista se iran guardando la posicion de las filas que se vayan ingresando para asi despues verificar si se uso esta posicion o no
    columna_usada = [] # Hace lo mismo que la lista de arriba pero con las columnas

    while True:
        print("\n---- Tablero ----")
        mostrar(tabla)
        print("Ingrese coordenada de la fila:")
        posicion_fila = coordenadas()
        print("Ingrese coordenada de la columna:")
        posicion_columna = coordenadas()
        # Este if invocara la funcion y si retorna True entrara, imprimira y despues ejecuta el continue que corta el bucle ahi y lo empieza otra vez, diferente al break que termina el bucle
        if verificar_coordenada_repetida(posicion_fila, posicion_columna, fila_usada, columna_usada):
            print("\n¡Ya ingresaste esa coordenada! Intenta con otra")
            continue
        # Este if verifica si esta la bomba en las coordenadas, si esta imprime
        if posicion_fila == fila_bomba and posicion_columna == columna_bomba:
            print("\n¡Boom! Perdiste")
            tabla[posicion_fila][posicion_columna] = "x" # Pone una 'x' donde esta la bomba
            mostrar(tabla)
            break
        # Si no entra a ninguno de los if significa que las coordnadas no habian sido usadas y tampoco estaba la bomba, entonces se sigue con lo siguiente
        tabla[posicion_fila][posicion_columna] = "o" # Pone una 'o' para marcar que se uso esa celda
        fila_usada.append(posicion_fila) # Agrega la posicion de la fila ingresada al final de la lista, eso hace append()
        columna_usada.append(posicion_columna) # Lo mismo de arriba pero con la columna
        print("\n¡Vas bien!")
        print(f"\nIntentos: {intento}")
        print(f"Celdas correctas: {celdas_correctas}")
        intento += 1
        celdas_correctas += 1
        
ejecutar()