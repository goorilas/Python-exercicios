# código para botar a cor no texto   \033[ style;text;back m. escrever o código a
# frente do texto depois das '', e no final para limitar a configuração de texto até onde deseja.
# formatar cores pare usar os nomes ao invéz dos códigos...
nome = 'weverson'
cores = {'limpa' : '\033[m' ,
         'azul' : '\033[34m' ,
         'amarelo' : '\033[33m' ,
         'pretoebranco' : '\033[7;30'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!' .format(cores['azul'], nome, cores['limpa']))
