x = input("Número 1: ")
y = input("Número 2: ")
z = input("Número 3: ")

x = float(x)
y = float(y)
z = float(z)



if x > y and x>z:
    if y > z:
            mayor = x
            mediano = y
            menor = z
    else:
            mayor = x
            mediano = z
            menor = y
elif y > z and y>x:
        if x > z:
            mayor = y
            mediano = x
            menor = z
        else:
            mayor = y
            mediano = z
            menor = x
else:
    if x > y:
            mayor = z
            mediano = x
            menor = y
    else:
        mayor = z
        mediano = y
        menor = x
        
print("Mayor:", mayor)
print("Mediano:", mediano)
print("Menor:", menor)