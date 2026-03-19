divisas = { "Euro" : "€", "Dollar" : "$", "Yuan" : "¥"}

opcion = input("Que divisa desea ver?: \n")

opcion = opcion.title()



if opcion in divisas:
    print(f"Su divisa esta en la lista: {(divisas[opcion])} {opcion}")
else:
    print("Su divisa no esta en la lista.")