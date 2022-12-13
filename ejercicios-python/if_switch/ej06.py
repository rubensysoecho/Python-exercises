# Solución con IF
num1 = input("Número 1: ")
num2 = input("Número 2: ")
num3 = input("Número 3: ")

float(num1)
float(num2)
float(num3)

if (num1 < num2):
    if (num1 < num3): min = num1
    else: min = num3
elif (num2 < num1):
    if (num2 < num3): min = num2
    else: min = num3

print(f"El número más pequeño es el {min}")

# Solución nº1
# num1 = input("Número 1: ")
# num2 = input("Número 2: ")
# num3 = input("Número 3: ")

# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)

# numeros = [num1, num2, num3]

# print(min(numeros))
