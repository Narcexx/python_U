texto = "Hola Mundo"
print(texto)
print(texto[0])
print(texto[0:3])
print(texto.upper())
print(texto.lower())
print(texto.capitalize()) #El primer caracter lo pasa a mayuscula
print(texto.title()) #Pasa a mayuscula el primer caracter de cada palabra que tenga el sting
print(texto.strip()) #Elimina los espacios qu esten a las izquierda y a la derecha de la cadena de texto y si solo se quiere borrar un lado seria .rstrip() derecha - / .lstrip() izquierda
print(texto.find("M")) #find() te da el indice
print(len(texto)) #funcion que da la longitud del string este caso seria de valor 10
print(texto.replace("Mun", "XD"))
nuevoTexto = texto.replace("Mun", "XD")
print(texto, nuevoTexto)
print("Hola" in texto)  # in "variable" te devuelve un boolean
print(f"hola este es un print para el ejemplo de formateo de strings {texto}")
ejemplo = "Probando \"las comillas\"" #igual puede ser 'Probando "las comillas"'
print(ejemplo)
print(ejemplo, "\nSalto de linea")
print("xd", "lol", "a", sep="-") # sep= es un argumento de palabra clave, igual esta end= , solo se usan en print, en este caso usa un guión, en lugar de un espacio, para separar los argumentos