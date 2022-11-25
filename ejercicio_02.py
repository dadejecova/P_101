

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
