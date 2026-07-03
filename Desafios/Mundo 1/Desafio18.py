from math import sqrt
print('===== DESAFIO 18 =====')
adja = float(input('Informe o cateto adjacente: '))
opos = float(input('Informe o cateto oposto: '))
hipo = sqrt(adja ** 2 + opos ** 2)
print('\n')
print('===== Resposta =====')
print('Cateto adijacente: {} \n'
      'Cateto oposto: {} \n'
      'Hipotenusa: {:.2f}'.format(adja, opos, hipo))
