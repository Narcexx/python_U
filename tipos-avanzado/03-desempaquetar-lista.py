numeros = [1, 2, 3, 4, 5, 6, 7]

# Manera horrible de hacer
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Mejor manera
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

primero, segundo, *otros, penul, ultimo = numeros
print(primero, segundo, ultimo, penul, otros)
