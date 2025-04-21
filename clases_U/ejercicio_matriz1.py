# Escribe una función que tome una matriz cuadrada como entrada y muestre la suma de todos sus elementos.
import random

# Funcion que crea la matriz
def crear_matriz():
    matriz = [] # Ss declara una matriz
    for i in range(3): # Este for es para ir creando las filas, el for terminara cuando se llegue al numero de filas establecida
        fila = [] # Se crea una lista que se llame fila
        for j in range(3): # Este for ira pasando por las columnas, el for terminara cuando se llegue al numero de columnas establecida
            valor = random.randint(3,6)  # Se crea una variable que guarde numeros randoms entre el 3 y 6
            fila.append(valor) # Aqui con el metodo .append() agregara el valor a la lista fila, lo que hace append es agregar un elemento al final de la lista
        matriz.append(fila) # Cuando termine el for de las columnas, significa que se le agrego un valor a todas las columnas de esa fila, entonces se agrega la lista fila a la matriz
        # Despues se creara otra fila y repite el procedimiento
    return matriz # Al finalizar los for, retornara la matriz creada


# Funcion que sumara los datos de la matriz, recibe como parametro la matriz
def suma_matriz(matriz):
    resultado = 0
    for i in range(3): # Este for es para ir pasando por las filas, el for terminara cuando se llegue al numero de filas establecida
        for j in range(3): # Este for ira pasando por las columnas y sumando, el for terminara cuando se llegue al numero de columnas establecida
            resultado +=  matriz[i][j] # Va a ir sumando los valores hasta que recorra toda la fila
            
    return resultado # Al finalizar los for, retornara el resultado

print(crear_matriz()) # Muestra la matriz
resultado = suma_matriz(crear_matriz()) # Se crea la variable resultado para guardar este mismo invocando la funcion sumar_matriz() y pasandole como argumento crear_matriz()
print(f"La suma de todos los elementos de la matriz es: {resultado}")