# Adivinar un numero

print("_____________________")
print("Adivinar un número")
print("_____________________")

import random

N_A = random.randint(1, 10)

print("Adivina el numero entre 1 y 10.")

while True:
    adv = int(input("Introduce tu adivinanza: "))
    
    if adv < N_A:
        print("El numero es mayor.")
    elif adv > N_A:
        print("El numero es menor.")
    else:
        print("felicidades usuario,has adivinado el número.")
        break

print("FIN DEL PROGRAMA")