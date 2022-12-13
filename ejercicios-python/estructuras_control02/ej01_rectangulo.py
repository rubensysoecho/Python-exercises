x1 = int(input("(x1,y1) x1 = "))
y1 = int(input("(x1,y1) y1 = "))
print()
x2 = int(input("(x2,y2) x2 = "))
y2 = int(input("(x2,y2) y2 = "))

base = x2 - x1
altura = y2 - y1
area = base * altura

print()
print("El rectángulo tiene", base, "cm de base y", altura, "cm de altura.")
print("El área del rectángulo es de", area, "cm.")