# Sumar números hasta un límite

# Establecer el límite de suma
limite_suma = 100

suma = 0

# Utilizacion de bucle while
while suma < limite_suma:
    
  numero = float(input("Ingrese un número entero positivo (o 0 para terminar): "))

  if numero == 0:
    break

  suma += numero

# Mostrar la suma final
print("La suma de los números ingresados es:", suma)

print("FIN DEL PROGRAMA")