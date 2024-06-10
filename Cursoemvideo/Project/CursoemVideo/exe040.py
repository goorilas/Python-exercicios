#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programam também deverá mostra o tempo que falta ou que ja passou do prazo.
from datetime import date
nacido = int(input('Por favor digite o ano do seu nascimento:   '))
hoje = date.today().year
idade = hoje - nacido
if idade < 18:
    print('Você ainda vai fazer o alistamento militar.')
    saldo = 18 - idade
    print('Ainda faltam {} anos para vc se alistar.' .format(saldo))
elif idade == 18:
    print('É hora de se alistar!!!')
elif idade > 18:
    saldo = idade - 18
    print('Já passou do tempo de se alistar..')
    print('Se passaram {} anos des de que você completou a idade para o alistamento.' .format(saldo))
