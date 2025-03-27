def hola(): # definimos la funcion
    print("hola mundo")

hola() # llamamos a la funcion


def bienvenido(nombre, apellido): # definimos la funcion y le agregamos parametros
    print(f"Bienvenido {nombre} {apellido}")

bienvenido("Manuel", "Rubilar") # llamamos a la funcion y le agregamos los argumentos o valores que tendran los parametros en la funcion
bienvenido("Marcelinho", "Nunez")


def bienvenido(nombre, apellido = "xd" ): 
    print(f"Bienvenido {nombre} {apellido}")

bienvenido("Manuel", "Rubilar") 
bienvenido("Marcelinho")


def bienvenido(nombre, apellido): 
    print(f"Bienvenido {nombre} {apellido}")

bienvenido(apellido = "Gaymin", nombre = "Narce") # Se puede cambiar el orden los argumentos, pero se tienen que nombrar con los parametros que pertenecen