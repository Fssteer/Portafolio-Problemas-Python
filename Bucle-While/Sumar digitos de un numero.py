# Sumar digitos de un numero

# Solicitar un número entero al usuario
numero = int(input("Ingrese un número entero: "))

suma_digitos = 0

# Utilizacion del bucle while
while numero > 0:
  digito = numero % 10
  suma_digitos += digito
  numero //= 10

# Mostrar la suma de dígitos
print("La suma de los dígitos del número es:", suma_digitos)

print("FIN DEL PROGRAMA")
