import math as mt

a = input("Valor de a: ")
b = input("Valor de b: ")
c = input("Valor de c: ")

a = float(a)
b = float(b)
c = float(c)

x1 = ((b * -1) + mt.sqrt(b** - 4 * a * c)) / 2 * a
x2 = ((b * -1) - mt.sqrt(b** - 4 * a * c)) / 2 * a

print("X1 -->", round(x1, 3), " X2 -->", round(x2, 3))