# Determinar si un año es un siglo

def es_primer_año_siglo(año):
 

  if año <= 0:
    
    return False

  año_sin_digitos = año // 100

  if año_sin_digitos == 0:
    return True

  return False

año = int(input("Ingrese un año: "))

if es_primer_año_siglo(año):
  print(f"El año {año} es el primer año del siglo.")
else:
  print(f"El año {año} no es el primer año de un siglo.")
