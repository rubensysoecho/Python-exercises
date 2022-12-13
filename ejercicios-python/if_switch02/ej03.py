x = input("Número 1: ")
y = input("Número 2: ")
z = input("Número 3: ")

x = float(x)
y = float(y)
z = float(z)

if x + 1 != y:
    consecutivo = False
else:
    if y + 1 != z:
        consecutivo = False
    else:
        consecutivo = True
        
if consecutivo == True:
    print("Los números son consecutivos.")
else:
    print("Lós números NO son consecutivos.")