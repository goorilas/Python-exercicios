print('-=-' * 20)
print('\033[34mAnalizador de triangulos\033[m.')
print('-=-' * 20)
a = float(input('Primeiro lado:  '))
b = float(input('Segundo lado:  '))
c = float(input('Terceiro lado:  '))
if a + b < c or a + c < b or b + c < a:
    print('Não é um triangulo')
else:
    print('Pode formar um triangulo')
    if a == b and a == c and b == c:
        print('Esse triangulo é EQUILATERO.')
    elif a == b != c or b == c != a or c == a !=b:
        print('Esse triangulo é ISÓSCELES.')
    elif a != b and b != c and c != a and c != b:
        print('Esse triangulo é ESCALENO')