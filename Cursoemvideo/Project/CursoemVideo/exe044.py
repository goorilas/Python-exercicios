peso = float(input('Digite seu peso atual:Kg  '))
altura = float(input('Digite sua altura:  '))
imc = peso / (altura ** 2)
print('Seu indice de massa corporal é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso ideal!!!')
elif imc > 18.5 and imc < 25:
    print('Você esta no peso ideal!!!')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso!!!')
elif imc > 30 and imc <= 40:
    print('VocÊ esta com obesidade!!!')
else:
    print('Você esta com obesidade mórbida!!!')
