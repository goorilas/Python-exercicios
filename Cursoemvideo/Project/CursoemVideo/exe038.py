#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para primário/ 2 para octal/ 3 para hexadecimal.
numero = int(input('Digite um numero para ser convertido:   '))
bina = format(numero, 'b')
octa = format(numero, 'o')
hexa = format(numero, 'x')
print('Digite \033[34m1\033[m para binário, \033[34m2\033[m para octal e \033[34m3\033[m para hexadecimal')
resultado = int(input('Sua opção foi:  '))
if resultado == 1:
    print(bina)
elif resultado == 2:
    print(octa)
elif resultado == 3:
    print(hexa)





