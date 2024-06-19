# Determinar la categoria de un trabajador

def determinar_categoria(años_experiencia):

  if años_experiencia < 2:
    categoria = "Junior"
  elif años_experiencia < 5:
    categoria = "Semi-Senior"
  else:
    categoria = "Senior"
  return categoria

años_experiencia = int(input("Ingrese la cantidad de años de experiencia: "))

categoria = determinar_categoria(años_experiencia)

print(f"La categoría del trabajador es: {categoria}")
