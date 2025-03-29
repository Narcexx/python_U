temperatura = float(input("Ingrese temperatura a convertir:"))
escala = input("Es Fahrenheit(F) o Celsius(C):").upper()
if escala == "F":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "C":
    fahreheit = (temperatura * 9/5) + 32
    print(fahreheit)
else:
    print("Escala incorrecta")
