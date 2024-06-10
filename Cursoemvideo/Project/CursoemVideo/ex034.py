salario = float(input('Qual o valor do seu salário:  '))
s1 = salario * 10 / 100
s2 = salario * 15 / 100
if salario > 1250:
    print('Seu aumento de salário é de 10%, R${}.' .format(s1))
    print('O valor total fica R${:.2f}.' .format(salario + s1))
if salario <= 1250:
    print('Seu aumento de salário é de 15%, R${}' .format(s2))
    print('O valor total fica R${:.2f}' .format(salario+s2))