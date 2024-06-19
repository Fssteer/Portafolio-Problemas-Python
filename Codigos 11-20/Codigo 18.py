# Determinar si un numero es divisible por 3 y 5

numero = int(input("Ingrese un número: "))

# Determinar si es divisible por 3, por 5, por ambos o por ninguno
if numero % 3 == 0 and numero % 5 == 0:
    print("El número es divisible por 3 y 5")
elif numero % 3 == 0:
    print("El número es divisible por 3")
elif numero % 5 == 0:
    print("El número es divisible por 5")
else:
    print("El número no es divisible ni por 3 ni por 5")