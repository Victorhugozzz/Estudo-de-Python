print('\033[31m===== DESAFIO 26 =====\033[m')
variavel = str(input('\033[1;32mDigite uma frase: \033[m'))

print ('Na palavra {} '.format(variavel), end='')
print ('tem {} lentras A '.format(variavel.count('a' or 'A')))
print ('A letra A aparece a primeira vez na posição numero {}'.format(variavel.find('a' or 'A')))
print ('A letra A aparece a última vez na posição numero {}'.format(variavel.rfind('a' or 'A')))
