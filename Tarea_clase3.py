
#conceptos basicos, operadores.
precio = 60
cantidad = 4

#calculo de la compra
total = precio * cantidad

#sentencia if
if total > 100:
    print("Tienes un descuento del 10%")
else:
    print("No aplica descuento")

#bucles y funciones, for
productos = ["Mouse", "Teclado", "Monitor", "USB", "Audífonos"]
for i in range(len(productos)):
    print(i, productos[i])

numero_secreto = 0

while numero_secreto != 44:
    numero_secreto = int(input("Adivina el número secreto: "))
    if numero_secreto == 44:
        print("Adivinaste el número secreto")
    else:
        print("No adivinaste el número secreto")

def calcular_total(precio, cantidad):
    return precio * cantidad

print(f"total de estos {cantidad} productos que cuestan ${precio} es: {calcular_total(precio, cantidad)}")

#estructura de datos arrays, listas, tuplas y diccionarios
#lista
precios = [10, 20, 30, 40, 50]

#tupla
categorias = ("Electrónica", "Accesorios", "Periféricos")

#diccionario
producto = {
    "nombre": "Mouse",
    "precio": 10,
    "cantidad": 2
}