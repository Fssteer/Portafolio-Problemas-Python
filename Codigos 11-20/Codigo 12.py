# Calcular el salario neto

salario_bruto = float(input("Ingrese su salario bruto: "))

if salario_bruto > 2000:
  impuesto = salario_bruto * 0.2
else:
  impuesto = 0

salario_neto = salario_bruto - impuesto

print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Impuesto: {impuesto:.2f}")
print(f"Salario neto: {salario_neto:.2f}")
