#Escreva um progrma que leia dois números inteiros e compare-os, mostrando na tela uma imagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
pri = int(input('Digite o primeiro numero inteiro:  '))
seg = int(input('Digite o segundo numero inteiro:   '))
if pri > seg :
    print('O primeiro valor é maior!')
elif seg > pri :
    print('O segundo valor é maior!')
elif pri == seg:
    print('Não existe valor maior, os dois são iguais')