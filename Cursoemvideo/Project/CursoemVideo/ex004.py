n = input('Digite algo: ')
print('o tipo primitivo desse valor é', type(n))
print('Só tem espaços?', (n.isspace()))
print ('É um numero?',(n.isnumeric()))
print ('É alfabético?',(n.isalpha()))
print ('É alfanumerico?',(n.isascii()))
print ('É decimal?',(n.isdecimal()))
print ('É um digito?',(n.isdigit()))
print ('Está em maiúsculas?', (n.isupper))
print ('Está em minúsculas?', (n.islower))
print ('Está capitalizada?', (n.istitle))


