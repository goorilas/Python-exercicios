print('{:=^40}' .format('LOJAS DRAYSY')) #CONFIGURAÇÃO PARA CENTRALIZAR O TEXO ESCRITO.

valor = float(input('Qual o valor da compra?R$ '))
avista = valor - (valor * 10 / 100)
avistac = valor - (valor * 5 / 100)
cartão2x = valor
cartão3x = valor + (valor * 20 / 100)
duasvezes = valor / 2

print('1. Pagamento à vista(dinheiro ou cheque), com 10% de desconto')
print('2. Pagamento à vista no cartão com 5% de desconto.')
print('3. Em até duas vezes no cartão com o preço normal.')
print('4. Em tres vezes ou mais no cartão com 20% de juros.')
escolha = int(input('\033[34mEscolha uma das formas de pagamento acima:\033[m  '))
if escolha == 1:
    print('Você escolheu a forma de pagamento a vista (dinheiro ou cheque), com 10% de desconto.')
    print('O valor da sua compra sera de R${:.2f} reais. ' .format(avista))
elif escolha == 2:
    print('Você escolheu a forma de pagamento (a vista no cartão), com 5% de desconto.')
    print('O valor da sua compra será de R${:.2F} reais.' .format(avistac))
elif escolha == 3:
    print('Você escolheu a forma de pagamento de (duas vezes no cartão), com o valor normal da compra.')
    print('O valor da sua compra será de R${:.2F} reais, em duas parcelas de R${:.2F} reais.' .format(cartão2x, duasvezes))
elif escolha == 4:
    print('Você escolheu a forma de pagamento de (tres vezes ou mais no cartão), com 20% de juros.')
    if escolha == 4:
        parcelas = int(input('Quantas parcelas?  '))
        juros = cartão3x / parcelas
        print('O valor da sua compra vai ser de R${:.2F} reais, com {} parcelas de R${:.2F} ao mês.' .format(cartão3x, parcelas, juros))
else:
    print('FALHA NO SISTEMA')
    print('TENTE NOVAMENTE!!!')