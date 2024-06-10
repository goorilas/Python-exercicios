# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode esceder 30% do salário ou então o emprestimo será negado.
print("-=-" * 40)
analizador = '\033[34mANALIZADOR DE CRÉDITO IMOBILIÁRIO\033[m'
print(analizador.center(109, '='))
print("-=-" * 40)
casa = float(input('Qual o valor do imóvel que deseja adquirir?R$   '))
salario = float(input('Qual o valor do seu salário mensal? R$  '))
anos = int(input('Em quantos anos vai pagar o imóvel:   '))
mensalidades = casa / (anos * 12)
mínimo = (salario * 30 / 100)
print('Para pagar uma casa de R${}, em {} anos, o valor mensal seria R${:.2f}.' .format(casa, anos, mensalidades))
if mensalidades >= mínimo:
    print('Seu crédito foi NEGADO!')
else:
    print('Seu crédito foi APROVADO!')