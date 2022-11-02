num1 = input("Introduce un número: ")
num2 = input("Introduce un número: ")

num1 = float(num1)
num2 = float(num2)

if num1 % num2 == 0:
    print("El número", int(num2), "es divisor de", int(num1))
else:
    print("El número", int(num2), "NO es divisor de", int(num1))