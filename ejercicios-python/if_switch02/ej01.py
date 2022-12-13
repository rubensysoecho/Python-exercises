num = input("Introduce un número real: ")
tipo_moneda = input("Introduce un tipo de moneda (euro/peseta): ")

num = int(num)

if tipo_moneda != "euro" and tipo_moneda != "peseta":
    print("El tipo de moneda no es correcto.")
else:
    if tipo_moneda == "peseta":
        resultado = num * 166.3860
        print(num, "euros -->", resultado,"pesetas")
    else:
        resultado =  num / 166.3860
        print(num, "pesetas -->", resultado,"euros")
