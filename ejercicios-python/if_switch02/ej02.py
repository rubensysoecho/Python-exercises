x = input("Número 1: ")
y = input("Número 2: ")
z = input("Número 3: ")

x = float(x)
y = float(y)
z = float(z)

if x > y:
    ordenado = False
else:
    if y > z:
        ordenado = False
    else:
        ordenado = True
        
if ordenado == True:
    print("Los números están ordenados.")
else:
    print("Lós números NO están ordenados.")