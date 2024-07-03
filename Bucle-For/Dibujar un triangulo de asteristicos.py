# Dibujar un triangulo de asteriscos

("/Dibujar un triángulo de asteriscos/")


for altura in range(1, 6):

  espacios = altura - 1
  
  for _ in range(espacios):
    print(" ", end="")
  for _ in range(altura):
    print("*", end="")
  print() 
