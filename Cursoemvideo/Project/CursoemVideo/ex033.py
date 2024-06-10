numero1 = int(input('Digite o primeiro numero:  '))
numero2 = int(input('Digite o segundo numero:  '))
numero3 = int(input('Digite o terceiro numero:  '))
#verificando quem é maior.
maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
print ('Maior:', maior)
#verificando quem é menor.
menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print('Menor:', menor)
