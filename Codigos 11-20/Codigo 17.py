# Determinar el tipo de licencia de conducir

edad = int(input("Ingrese su edad: "))

if edad >= 16 and edad <= 17:
    print("Licencia de menor")
elif edad >= 18 and edad <= 65:
    print("Licencia de adulto")
else:
    print("Licencia de adulto mayor")