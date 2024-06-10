print('=-=' * 50)
print('OLÁ CARO ALUNO! VAMOS VER SUA MÉDIA!')
print('=-=' * 50)
nota1 = float(input('Por favor digite sua primeira nota:  '))
nota2 = float(input('Por favor digite a sua segunda nota:  '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média atual é {}, sinto lhe informar que va foi REPROVADO!' .format(media))
elif media > 5 and media < 7:
    print('Você tera que fazer recuperação.')
elif media >= 7:
    print('APROVADO')