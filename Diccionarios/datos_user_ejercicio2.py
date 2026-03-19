
info = {"nombre" : "", "Edad" : "", "Direccion" : "", "Telefono" : ""}

for i in info:
    dato = input(f"Cual es tu {i}?: ")
    info[i] = dato

print(f"{(info['nombre'])} tiene {(info['Edad'])} años, Vive en {(info['Direccion'])} y su numero de telefono es: {(info['Telefono'])}")