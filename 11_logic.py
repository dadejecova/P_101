# AND
print('AND')
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and False =>", False and False)


stock = input("Ingrese el número de Stock =>")
stock = int(stock)

print(stock >= 100 and stock <= 1000) 

# or
print('OR')
print("True or True =>", True or True)
print("True OR False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

role = input("Digita el rol =>")

print(role == "admin" or role == "seller")