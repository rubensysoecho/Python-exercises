altura = input("Introducza la altura, en metros: ")
altura = float(altura)

radio = input("Introduzca el radio, en metros: ")
radio = float(radio)

pi = 3.1416
volumen = pi * (radio**2) * altura

print("El volumen del cilindro es de ", round(volumen, 2), " metros cúbicos")