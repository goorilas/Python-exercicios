carro = float(input('Qual é a velocidade atual do carro?   '))
multa = (carro - 80) * 7
if carro <=80:
    print('Você esta dentro do limite de velocidade.')
    print('\033[4;32;44mTenha um bom dia, dirija com segurança!\033[m')
else:
    print('\033[4;31;44mVocê estava ah {:.2f} Km/h, e foi multado em R${:.2f} por esceder o limite de velocidade.\033[m' .format(carro,multa))
# código para botar a cor no texto   \033[ style;text;back m. escrever o código a frente do texto depois das '', e no final para limitar a configuração de texto até onde deseja.