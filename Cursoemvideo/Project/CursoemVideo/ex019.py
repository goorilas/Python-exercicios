import random
# from random import choice
aluno = input('Digite o nome do primeiro aluno:   ')
aluno2 = input('Digite o nome do segundo aluno:  ')
aluno3 = input('Digite o nome do terceiro aluno:  ')
aluno4 = input('Digite o nome do quarto aluno:  ')
lista = [aluno, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O aluno vencedor é: {}" .format(escolhido))



