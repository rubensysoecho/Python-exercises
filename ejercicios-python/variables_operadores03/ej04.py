segundosEnunciado = 500000
diasCompletos = segundosEnunciado / (24 * 60 * 60)
segundosDiaIncompleto = segundosEnunciado % (24 * 60 * 60)
horasCompletas = segundosDiaIncompleto / (60 * 60)
segundosHoraIncompleta = segundosDiaIncompleto % (60 * 60)
minutosCompletos = segundosHoraIncompleta % 60
segundosMinutoIncompleto = segundosHoraIncompleta % 60
print(segundosEnunciado, "segundos=", diasCompletos,"dias,",horasCompletas,"horas,",minutosCompletos,"minutos y",segundosMinutoIncompleto,"segundos")