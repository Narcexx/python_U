saludo = "Hola global"

def saludar():
    saludo = "Hola mundo"
    print(saludo)

def saludame():
    saludo = "Hola tu"
    print(saludo)

# Se queria demostrar aca que las variables son independientes en cada funcion, no importa si tienen el mismo nombre como en este caso la variable saludo
# Tendriamos que definir la variable afuera de las funciones para que sea global, como se hizo al principio del codigo
# Para llamar una variable dentro una fucnion que este afuera hay que poner 'global "nombre de la variable"', hay una discusion con respecto a esto que se dice que es una mala practica
# Asi que evitar usar variables globales

saludar()
saludame()
saludar()
print(saludo)