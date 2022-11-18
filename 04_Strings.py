nombre = "Daniel"
apellidos = "Coello"
edad = 28
print(nombre)
print(apellidos)

full_name = nombre + " " + apellidos
print(full_name)

quote = "I'm Daniel"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# Format

template = "Hola version 1, mi nombre es " + nombre + " y mi apellido es " + apellidos + "."
print(template)

templae = "Hola version 2, mi nombre es {} y mi apellido es {}".format(nombre, apellidos)
print(template)

template = f"Hola version 3, mi nombre es {nombre} y mi apellido es {apellidos}. Y mi edad es {edad}."
print(template)