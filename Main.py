"""
adicao = 72 + 23
subtracao = 108 - 304
multiplicacao = 108 * 0.5
divisao = 108 / 9
exponenciacao = 2 ** 3

print(adicao + subtracao + multiplicacao)


refeicao = 64.54
taxa = 1.1
total = refeicao * taxa
print("R$ %.2f" % total)


refeicao = 50.00
taxa_de_servico = 1.1
total = refeicao * taxa_de_servico

print("R$ %.4f" % total)

nome = "Marcos"
quantidade_caracteres = len(nome)
print(quantidade_caracteres)
print(nome[quantidade_caracteres - 1].upper())


valor = 1979.0399
print("R$ " + str(valor))
print("R$ %.2f" % valor)


nome = "Marcos"
sobrenome = "Cascino"
print(nome + " " + sobrenome.upper())
print((nome + " " + sobrenome).upper())
print(len(nome + " " + sobrenome))


nome = "Marcos"
sobrenome = "Cascino"
idade = 37
trabalho = "UniÍtalo"
profissao = "ADM"
Data_nascimento = 3/11/1979

import datetime

hoje = datetime.date.today()

AnoAtual = hoje.strftime("%Y")

meses = { 'janeiro' : 1, 'fevereiro' : 2, 'marco' : 3, ' abril ' : 4,  'maio ' : 5, 'Junho' : 6, 'julho' : 7, 'agosto' : 8, 'setembro'
: 9, 'outubro' : 10, 'novembro' : 11, 'dezembro' : 12}

meses1 = {1 : 'janeiro' , 2 : 'fevereiro',  3 : 'marco', 4 :  ' abril ', 5:  'maio ',  6 : 'Junho', 7 : 'julho', 8 : 'agosto', 9: 'setembro',
10 : 'outubro', 11: 'novembro',  12 : 'dezembro' }

bissexto = False

coletandodados = True

while coletandodados == True:
    dia = input("03")
    mes = input("11")
    mes = input("11")



print("{1}\n{0}".format(nome, sobrenome))


print("{0}\n{1}\n{2}\n{3}".format(nome, sobrenome, idade, trabalho, profissao))

import datetime

data1 = datetime.date(day=22, month=11, year=2013)

data2 = datetime.date(day=25, month=3, year=2017)

print(data2-data1)

from datetime import date
hj = date.today()
print(date.today)

"""

""" 
import time

print(time.strftime("%h:%M:%S"))

print(time.strftime("%I:%M:%S"))

print(time.strftime("%d/%m/%Y"))

def calculate_age(born):
    data_de_nascimento = 3/11/1979
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    print(date.today - data_de_nascimento)

import datetime

Birthday = datetime.datetime (1979,3,11)
diference = datetime.datetime.now() - Birthday

"""


minutos = 2
baterias = 100
pedras = (minutos * baterias * 300) / (15 * 5)

print(pedras)
print("A Catapulta lançará {:.0f} pedras em {} baterias de {} minutos cada.".format(pedras, baterias, minutos))










