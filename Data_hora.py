
"""import datetime

data1 = datetime.date(day=22, month=11, year=2013)

data2 = datetime.date(day=25, month=3, year=2014)

data2-data1

datetime.timedelta(123)

diferenca = data2-data1

print(diferenca.days)
"""

from datetime import datetime

agora = datetime.now()

print(agora.day)

dia = agora.day
mes = agora.month
ano = str(agora.year)[2:4]

print("\t{}/{:02d}/{}".format(dia, mes, ano))

hora = agora.hour
minutos = agora.minute
segundos = agora.second

#usar \ para escapar caracteres
print("\t\t\t\t{:02d}h{:02d}'{:02d}\"".format(hora, minutos, segundos))

