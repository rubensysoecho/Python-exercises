num = input("Introduzca un número: ")

num = float(num)

if num > 0:
    print(int(num), "> 0")
elif num < 0:
    print(int(num), "< 0")
else:
    print(int(num), "= 0")