numero = int(input('Digite um numero:  '))
if numero % 2 == 0:
    print('O numero {} é \033[34mpar.\033[m' .format(numero))
else:
    print('O numero {} é \033[34mimpar.\033[m' .format(numero))
# Para saber se um número é par ou ímpar, basta dividir ele por 2 usando o operador de resto da divisão.
#se for par, o resto sempre é 0. Se for impar, o resto sempre é 1.