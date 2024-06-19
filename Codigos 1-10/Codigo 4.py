# Determinar si un carácter es una vocal

letra = input("Digite una letra: ")

vocales = 'a','e','i','o','u','A','E','I','O','U'

if len(letra) == 1 and letra in vocales:
    print("Es una vocal")
    
else:
    print("No es una vocal")
    
print("Fin de programa")