# Clasificar la categoria

edad = float(input("Ingresa tu edad: "))
print("_______________________________________")
if edad >= 0 and edad <= 12:
    print("Segun su edad es un niño (infante).")
elif edad >= 13 and edad <= 19:
    print("Segun su edad usted es un adolescente.")
elif edad >= 20 and edad <= 59:
    print("Segun su edad usted es un adulto.")
else:
    print("Segun su edad usted es un adulto mayor.")

print("_______________________________________")

print("Fin programa")

