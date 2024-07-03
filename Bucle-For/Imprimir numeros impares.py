# Imprimir numeors impares

print ("/Imprimir números impares/")
numero = int(input("Introduce un número entero positivo: "))

print("Números impares del 1 al", numero, ":")
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)
