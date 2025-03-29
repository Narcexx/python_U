punto = {"x": 25, "y": 50} # El de la izquierdd es un string y el de la dececha puede se cualquier dato en este caso numeros
print(punto)
print(punto["x"]) # No se puede acceder a los valores como una lista o un set, hay que colocar el string en este caso "x"
print(punto["y"])

punto["z"] = 45 # Crear una llave en el diccionario
print(punto)
if "lala" in punto:
    print(f"Encontre lala {punto["lala"]}")

print(punto.get("x")) # Otro metodo para acceder a un valor del diccionario es el .get()
print(punto.get("lala", 97)) # Aca en caso que no estuviera el valor en el diccionario uno le puede dar valor por defecto que en este caso le puse 97
del punto["x"] # Esto elimina la llave y su valor
del(punto["y"]) # Esta funcion hace lo mismo
print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor]) # Muesta la llave y el valor y print(valor) solo motraria la llave

for valor in punto.items(): # Con esto te lo muesta como tuplas
    print(valor)

for llave, valor in punto.items(): # Esta lo muestra como el primer for 
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Manolo"},
    {"id": 2, "nombre": "Marce"},
    {"id": 3, "nombre": "Igna"},
    {"id": 4, "nombre": "Nacho"}
]

for usuario in usuarios:
    print(usuario["nombre"]) # Iteramos usuarios y despues le damos la llave que queremos acceder en este caso seria "nombres"