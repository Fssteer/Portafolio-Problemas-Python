# Convertir grados celsius a fahrenheit

print ("/Convertir grados Celsius a Fahrenheit:/")

inicio = int(input("Ingresa la temperatura inicial en grados Celsius: "))
fin = int(input("Ingresa la temperatura final en grados Celsius: "))

print("\nConversion de grados Celsius a Fahrenheit:")
for celsius in range(inicio, fin + 1):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
