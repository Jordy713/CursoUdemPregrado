name = "Jordy"

print(name)

numero = 3

print(numero)

verdad = True

if verdad:
    print(name)
else:
    print(numero)

listas = [1, 2, 3, 4, 5]

diccionario = {"nombre": "Jordy", "edad": 30}

for item in listas:
    print(item)

[print(item) for item in listas]

def miprimera_funcion(nombre):
    print(f"Hola, {nombre}")