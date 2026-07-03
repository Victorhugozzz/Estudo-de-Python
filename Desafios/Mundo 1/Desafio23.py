from itertools import count

nome = str(input('Digite seu nome completo: '))
print('===== DESAFIO 23 =====')
print('\n')
print('Seu nome em letras maiusculas: {}'.format(nome.upper()))
print('Seu nome em letras minusculas: {}'.format(nome.lower()))
print('Quantidade de letras (sem os espaços: {}'.format (len(nome) - nome.count(' ')))
print('Quantidade de letras no primeiro nome: {}'. format (len(nome.split()[0])))
