sueldos = [1000, 1200, 500, 700, 3000, 2200, 1000, 990, 540, 2000, 1500, 1400]
pos_actualizados = []

print(f"SUELDOS SIN ACTUALIZAR: {sueldos}")

for i in range(0, len(sueldos)):
    if sueldos[i] < 800:
        sueldos[i] += 100
        pos_actualizados.append(i + 1)

print(f"SUELDOS ACTUALIZADOS: {sueldos}")

for i in range(0, len(pos_actualizados)):
    print(f"El sueldo nº{pos_actualizados[i]} fué actualizado.")
