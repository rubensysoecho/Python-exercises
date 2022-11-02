salarioBruto = input("Salario bruto: ")
salarioBruto = float(salarioBruto)

irpf = 12/100

salarioNeto = salarioBruto - (salarioBruto * irpf)
print("Salario neto --> ", salarioNeto)