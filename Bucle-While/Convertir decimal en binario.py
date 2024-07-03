# Convertir de decimal a binario

# Solicitar un número entero positivo al usuario
numero_decimal = int(input("Ingrese un número entero positivo: "))

# Inicializar la cadena binaria vacía
binario = ""

# Usar un ciclo while para convertir a binario
while numero_decimal > 0:

  residuo = numero_decimal % 2

  binario = str(residuo) + binario

  numero_decimal //= 2

binario_invertido = binario[::-1]

# Mostrar el número binario
print("El número binario es:", binario_invertido)

print("FIN DEL PROGRAMA")

