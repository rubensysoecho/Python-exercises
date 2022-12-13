num1 = float(input("Introduce número 1: "))
num2 = float(input("Introduce número 2: "))

if num1 > num2:
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)
else:
    resultado = num2 - num1
    print(num2, "-", num1, "=", resultado)
    