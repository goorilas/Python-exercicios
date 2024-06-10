from datetime import date
ano = int(input('Digite um ano qualquer, ou coloque 0 para analizar o ano atual:  '))
if ano == 0:
    ano = date.today().year # esse codigo pega o ano atual da maquina que esta usado em questão.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto.' .format(ano))
else:
    print('O ano não {} é bisexto.' .format(ano))