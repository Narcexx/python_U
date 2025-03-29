mascotas = ["Lucy", "Nana", "Garu", "Lucy"]

print(mascotas.index("Nana"))
# print(mascotas.index("Nene")) Esto marca error porque no esta se previene asi
if "Nene" in mascotas:
    print(mascotas.index("Nene"))

print(mascotas.count("Lucy"))