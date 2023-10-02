print("Ingresa tu nombre:")
nombre = input()
print(type(nombre))
palabras = nombre.split(" ")
nombre = nombre.capitalize()
nombre = nombre.replace(" ", "-")

nombre_capitalizado = ""
for palabra in palabras:
    nombre_capitalizado += palabra.capitalize() + " "

nombre_capitalizado = nombre_capitalizado.strip()

print("HOLA: " + nombre_capitalizado)




