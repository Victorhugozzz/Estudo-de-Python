import random 
import time
print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)
print('\033[31mBem vindo ao jogo PAR OU IMPAR\033[m')

vitorias = 0

while True:
  print('-'*30)
  print('1 - Impar')
  print('2 - Par')
  jogador = int(input('Escolha [1] ou [2]: '))
  jogador_numero = int(input('Digite um valor entre 0 e 10: '))
  jogador_computador = random.randint(0,10)
  soma = jogador_computador + jogador_numero

  print('-'*30)
  print('PAR', end=' ')
  time.sleep(0.5)
  print('OU', end=' ')
  time.sleep(0.5)
  print('IMPAR')
  time.sleep(0.5)
  print('-'*30)

  if soma % 2 == 0:
    if jogador == 2:
      vitorias += 1
      print('A soma dos numeros deu {} e voce escolheu PAR, Parabéns, voce ganhou!'.format(soma))
    else:
      print('A soma dos numeros deu {} e voce escolheu IMPAR, Que pena, voce perdeu!'.format(soma))
      break
  else :
    if jogador == 1:
      vitorias += 1
      print('A soma dos numeros deu {} e voce escolheu IMPAR, Parabéns, voce ganhou!'.format(soma))
    else:
      print('A soma dos numeros deu {} e voce escolheu PAR, Que pena, voce perdeu!'.format(soma))
      break

print('-'*30)
print('FIM DO JOGO')
print('Voce obteve ')
print('Vitorias: {}'.format(vitorias))
print('-'*30)



