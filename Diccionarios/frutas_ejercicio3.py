#scribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {"platano":"1.35", "manzana" : "0.80", "pera" : "0.85", "naranja" : "0.70"}

opcion = input("Que fruta desea comprar?: ")
opcion = opcion.lower()

if opcion in frutas:
    kilos = int(input("Cuantos kilos desea llevar?: "))
    precio = kilos * float(frutas[opcion])
    print(f"Su total es de: ${precio} dolares")
else:
    print("Lo sentimos esa fruta no esta en el inventario.")