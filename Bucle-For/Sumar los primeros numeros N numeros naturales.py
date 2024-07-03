# Sumar los primeros N numeros naturales

print ("/Sumar los primeros N números naturales/")
n = int(input("Ingrese un número entero positivo: "))
total = 0
for numero in range(1, n + 1):
  total += numero
print(f"La suma de los primeros {n} números naturales es {total}")
