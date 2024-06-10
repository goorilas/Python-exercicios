frase = str(input('Digite uma fraze:  ')) .strip()
print('A letra (A) aparece {} vezes' .format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}' .format(frase.lower().find('a')+1))
print('A última letra A apareceu na posição {}' .format(frase.lower().rfind('a')+1))
