km = float(input('Qual a distância percorrida na sua viagem em Km?  '))
preço = km * 0.5
preço2 = km * 0.45
if km <= 200:
    print('O valor da sua viagem é de R${}' .format(preço))
else:
    print('O valor da sua viagem com desconto acima de 200Km é de R${:.2f}' .format(preço2))

#maneira simplificada
#preço = km * 0.50 if km <=200 else km * 0.45