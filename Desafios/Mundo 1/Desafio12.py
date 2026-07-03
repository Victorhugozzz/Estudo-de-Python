print('===== DESAFIO 12 =====')
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area= larg * alt
tinta = area / 2
print('Uma parede com a largura {} m e altura {} m \n'
      'tem uma área de {:.2f} metros quadrados.\n'
      'é necessário {:.2f} litros de tinta\n'.format(larg, alt, area, tinta))