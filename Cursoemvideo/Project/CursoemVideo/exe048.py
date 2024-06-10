soma = 0  # como começão em 0 vai dar o valor exato da soma dos valores abaixo.
cont = 0
for numero in range(1, 501, 2):
    if numero % 2 != 0:
        if numero % 3 == 0:
            cont += 1  # toda vez que ele achar um numero divizivel por 3 ele vai somar como mais um numero. += seria o msm que (cont = cont + 1)
            soma = soma + numero  # somar valores achados divisiveis por 3.
print('A soma dos {} numeros tem o valor de {}.'.format(cont, soma))
