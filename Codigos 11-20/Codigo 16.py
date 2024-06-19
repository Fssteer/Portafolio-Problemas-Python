# Clasificar el IMC

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura**2)

if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "gordo"

print(f"Su IMC es: {imc:.2f}")
print(f"Su clasificación es: {categoria}")