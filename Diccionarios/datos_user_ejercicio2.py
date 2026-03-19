#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje nombre tiene edad años, vive en dirección y su número de teléfono es teléfono

info = {"nombre" : "", "Edad" : "", "Direccion" : "", "Telefono" : ""}

for i in info:
    dato = input(f"Cual es tu {i}?: ")
    info[i] = dato

print(f"{(info['nombre'])} tiene {(info['Edad'])} años, Vive en {(info['Direccion'])} y su numero de telefono es: {(info['Telefono'])}")