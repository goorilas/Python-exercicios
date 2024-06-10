#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo, qual é o nome do homem mais velho, e quantas mulheres tem menos de 20 anos.
#--------------------------------------------------------------
médiaidade = 0
somaidade = 0
maioridadehomen = 0
homemmaisvelho = ''
for p in range(1, 5):
    print('-------{}ª------' .format(p))
    nome = str(input('Nome da pessoa:  ')) .strip
    idade = int(input('Idade:  '))
    sexo = str(input('Sexo F/M:  ')) .strip
    somaidade = somaidade + idade #ou (somaidade += idade) ------- que da na mesma.
    médiaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        homemmaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        homemmaisvelho = nome
print('A média de idade atual desse grupo é de {:.0f} anos.' .format(médiaidade))
print('O homem mais velho tem {:.0f} anos, e se chama {}.' .format(maioridadehomen, homemmaisvelho))