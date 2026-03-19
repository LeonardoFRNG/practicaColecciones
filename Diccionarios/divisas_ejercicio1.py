#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = { "Euro" : "€", "Dollar" : "$", "Yuan" : "¥"}

opcion = input("Que divisa desea ver?: \n")

opcion = opcion.title()



if opcion in divisas:
    print(f"Su divisa esta en la lista: {(divisas[opcion])} {opcion}")
else:
    print("Su divisa no esta en la lista.")