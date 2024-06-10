nome = str(input('Digite seu nome completo:  ')) .strip() #strip serve para eliminar os espaços antes e depois de uma string digitada.
print ('Analizando seu nome...')
print ('Seu nome em maiusculo é {}' .format (nome.upper()))
print ('Seu nome em minusculo é {}' .format(nome.lower()))
print ('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' '))) # usando essa formatação de nome.count(' ') vc elimina os espaços e conta só as letras.
print ('Seu primeiro nome tem {} letras' .format(nome.find(' '))) # nome.find (' ') conta tudo antes do primeiro espaço.
# Outro mode de se fazer a leitura do primeiro nome com o numero de letras.
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))

