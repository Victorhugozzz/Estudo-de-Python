import math
print('===== DESAFIO 19 =====')
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('\n')
print('===== Resposta =====\n')
print('O angulo {} tem: \n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}\n'.format(angulo, seno, cosseno, tangente))