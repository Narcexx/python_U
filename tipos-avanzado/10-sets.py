# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
# print(primer)
# primer.add(5)
# primer.remove(1)
# print(primer)
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)
# Operaciones que se pueden hacer con sets
print(primer | segundo) # hace una UNION
print(primer & segundo) # hace una INTERSECCION
print(primer - segundo) # hace una DIFERENCIA
print(primer ^ segundo) # hace una DIFERENCIA SIMETRICA

if 5 in segundo:
    print("Si esta")