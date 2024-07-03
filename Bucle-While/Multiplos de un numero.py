# Multiplos de un numero

# Solicitar número entero positivo al usuario
numero = int(input("Ingrese un número entero positivo: "))

contador = 1

# Utilizacion de bucle while
while contador <= 10:
 
  multiplo = numero * contador

  print(f"{numero} x {contador} = {multiplo}")

  contador += 1
