# Determinar si un numero es primo

print ("/Determinar si un número es primo/")

numero = int(input("Introduce un número entero positivo: "))
divisores = 0

for i in range(1, numero + 1):
    divisores += numero % i == 0

print(f"El número {numero} es primo." if divisores == 2 else f"El número {numero} no es primo.")
