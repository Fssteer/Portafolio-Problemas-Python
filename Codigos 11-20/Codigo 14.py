# Verificar si un triangulo es valido

lado_a = float(input("Ingrese la longitud del lado A: "))
lado_b = float(input("Ingrese la longitud del lado B: "))
lado_c = float(input("Ingrese la longitud del lado C: "))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
  print("Sí, es un triángulo válido.")
elif lado_a + lado_b == lado_c or lado_b + lado_c == lado_a or lado_a + lado_c == lado_b:
  print("Sí, es un triángulo, pero es degenerado (al menos dos lados tienen la misma longitud).")
else:
  print("No, no es un triángulo.")
