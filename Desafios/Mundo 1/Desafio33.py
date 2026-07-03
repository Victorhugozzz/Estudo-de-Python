print('===== DESAFIO =====')
ano = int(input('Digite um ano para ver se ele e bissexto: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print('{} nao e um ano bisssexto'.format(ano))
