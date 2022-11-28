if True:
    print("Debería ejecutarse")

if False:
    print("No debería ejecutarse")


stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto.")
else:
    print("El stock es incorrecto.")
    

pet = input("¿Cuál es tu mascota favorita?")

if pet == "perro":
    print("Tienes un buen gusto")
elif pet == "gato":
    print("tienes un gusto superior")
else:
    print("No has elegido algo digno.")