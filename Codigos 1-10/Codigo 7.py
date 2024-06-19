# Calcular el precio de descuento

precio = float(input("Digite el precio del producto:  "))

if precio > 100:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print(f"Se aplicó un descuento del 10%. El precio final después de aplicar el descuento es: ${precio_final:.2f}")
else:
    precio_final = precio
    print(f"No se aplicó ningún descuento. El precio final es: ${precio_final:.2f}")