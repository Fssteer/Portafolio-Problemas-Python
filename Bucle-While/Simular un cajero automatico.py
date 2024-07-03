# Simular un cajero automatico

# Establecer el PIN correcto
pin_correcto = "1234"

intentos = 0

# Utilizacion de bucle while
while intentos < 3:
 
  pin_ingresado = input("Ingrese su PIN: ")

  if pin_ingresado == pin_correcto:
    print("¡PIN correcto! Acceso concedido.")
    break  
  else:
    print("PIN incorrecto. Intentos restantes:", 3 - intentos - 1)
    intentos += 1  # Incrementar el contador de intentos

# Mensaje de bloqueo
if intentos == 3:
  print("¡Cuenta bloqueada! Contacte a su banco.")
  
print("FIN DEL PROGRAMA")
