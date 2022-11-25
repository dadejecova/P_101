lives = 3
print(type(lives))

age = 12
budget = 100

temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number_a = 450000000000000000.1
print(number_a)

number_b = 0.00000000000000001
print(number_b)



presupuesto_enero = input('Cual es tu presupuesto de Enero?')
presupuesto_febrero = input('Cual es tu presupuesto de Febrero?')
presupuesto_marzo = input('Cual es tu presupuesto de Marzo?')

presupuesto_enero= int(presupuesto_enero)
presupuesto_febrero= int(presupuesto_febrero)
presupuesto_marzo = int(presupuesto_marzo)

presupuesto_total = presupuesto_enero + presupuesto_febrero + presupuesto_marzo
presupuesto_avg = presupuesto_total/3
print(presupuesto_avg)

presupuesto_texto = f"El presupuesto que tenemos con respecto al primer trimestre es de: {presupuesto_avg}"
print(presupuesto_texto)

