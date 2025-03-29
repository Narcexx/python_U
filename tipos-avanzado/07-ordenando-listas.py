numeros = [2, 5, 7, 3, 1]

#numeros.sort() # ordena los elemenos, si se quiere ordenar al reves seria .sort(reverse=True)
numeros2 = sorted(numeros) # sorted igual ordena pero en diferencia con .sort() es que sorted crea una nueva lista sin modificar la original
#para hacer el orden al reves seria sorted('lista', reverse=True)
print(numeros)
print(numeros2)

usuarios = [[6, "xdd"], [2, "lol"], [4, "wtf"]]
# usuarios.sort()
# Ahora sale ordenado pq los numeros estan primero, pero si vinieran despues del string no se ordenarian, se puede arreglar creando una funcion asi
def ordena(elemento):
    return elemento[1] # indice 1 para que ordene a partir de ese elemento

usuarios.sort(key=ordena)
print(usuarios) 