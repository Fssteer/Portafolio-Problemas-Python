# Sumar numeros pares del 1 al 100

print ("/Sumar números pares del 1 al 100:/")
suma = 0
enumerador = 1

for  numero in range (1,101) :
	suma += numero
	enumerador +=2
	sumador_pares = enumerador // 2

print("------------------------------------------------")
print ("sumando los numeros pares es:",sumador_pares)
print("------------------------------------------------")