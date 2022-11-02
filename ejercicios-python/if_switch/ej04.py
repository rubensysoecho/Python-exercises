num = input("Introduzca un numero: ")
num = float(num)

if num > 10 :
    if num < 100:
        print("El número está entre 10 y 100.")
    else:
        print("El número es mayor que 100.")
else:
    print("El número es menor que 10.")