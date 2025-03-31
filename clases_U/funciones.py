# def hola(texto):
#     print(texto)

# hola("xd")
# hola("hola")
import math
def menu():
    print("\n🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
    print("🌟         📌 Calculadora 📌      🌟")
    print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
    print("🌟               MENU             🌟")
    print("🌟         ➕ 1️⃣  Sumar ➕         🌟")
    print("🌟         ➖ 2️⃣  Restar ➖        🌟")
    print("🌟         ✖️  3️⃣  Multiplicar ✖️    🌟")
    print("🌟         ➗ 4️⃣  Dividir ➗       🌟")
    print("🌟          √ 5️⃣  Raiz cuadrada √  🌟")
    print("🌟       🏃🚪 6️⃣  Salir 🏃🚪       🌟")
    print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")

def numeros():
     num1 = float(input("\n👉 Ingrese numero 1: "))
     num2 = float(input("👉 Ingrese numero 2: "))
     return num1, num2

def nuemero_raiz():
    num1 = float(input("👉 Ingrese numero: "))
    return num1

def operacion(op,num1, num2):
        if op == 1:
            tipo = f"suma es {num1 + num2}"
        elif op == 2:
            tipo = f"resta es {num1 - num2}"
        elif op == 3:
            tipo = f"multiplicacion es {num1 * num2}"
        elif op == 4:
            tipo = f"division es {num1 / num2}"
        return tipo
    
def operacionRaiz(op, num1):
    if op == 5:
        tipo = f"la raiz cuadrada de {num1} es {math.sqrt(num1)}"
        return tipo

def ejecutar():
    while True:
        menu()
        op = int(input("\n👉 Ingrese opcion: "))
        if op == 6:
           break
        elif op == 1 or op == 2 or op == 3 or op == 4:
            num1, num2 = numeros()
            print(f"\n🔥🔥 El resultado de la {operacion(op, num1, num2)} 🔥🔥\n")
        elif op == 5:
            numRaiz = nuemero_raiz()
            print(f"\n🔥🔥 El resultado de la {operacionRaiz(op, numRaiz)} 🔥🔥\n")
        else:
            print("👎 Ingrese una opcion valida 👎\n")

ejecutar()