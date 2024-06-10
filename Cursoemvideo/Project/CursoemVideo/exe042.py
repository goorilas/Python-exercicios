from datetime import date
from time import sleep

print('CONFEDERAÇÃO NASCIONAL DE NATAÇÃO')
sleep(1)
print('Classificação por idade')
sleep(1)
nacido = int(input('Por favor digite o seu ano de nacimento:  '))
hoje = date.today().year
idade = hoje - nacido

'''mirin =  idade <= 9
infantil = idade > 9 and idade <= 14
junior = idade > 14 and idade <= 19
senior = idade > 19 and idade <= 20
master = idade > 20'''

if idade <= 9:
    print('Sua idade é de {} anos, por tanto sua classificação é Mirin de 0 á 9 anos.' .format(idade))
elif idade > 9 and idade <=14:
    print('Sua idade é de {} anos, por tanto sua classificação é Infantil de 10 a 14 anos.' .format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é de {} anos, por tanto sua classificação é Junior de 15 a 19 anos.' .format(idade))
elif idade == 20:
    print('Sua idade é de {} anos, por tanto sua classificação é Sênior para idade de 20 anos.' .format(idade))
else:
    print('Sua idade é de {} anos, por tanto sua classificação é Master, acima de 20 anos.' .format(idade))