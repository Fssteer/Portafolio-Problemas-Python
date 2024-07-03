# Contar vocales en una cadena

print ("/Contar vocales en una cadena/")

vocales = "a,e,i,o,u,á,é,í,ó,ú,ü"
cadena_usuario = input("Ingrese una cadena de texto: ")
numero_vocales = sum(c in vocales for c in cadena_usuario.lower())
print(f"La cadena tiene {numero_vocales} vocales.")
