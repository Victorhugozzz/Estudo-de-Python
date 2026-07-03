import random
import time
print('===== \033[31mDESAFIO\033[m =====')
print('Bem vindo ao jogo\033[33m Jokenpô\033[m')
print('1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura\n')

player1 = int (input('Qual a sua jogada: '))
player2pc = random.randint(1, 3)

print('JO...')
time.sleep(0.5)
print('KEN...')
time.sleep(0.5)
print('PO!!!')

print('======================================')
if player1 == 1:
    print('O jogador  escolheu pedra'.format(player1))
elif player1 == 2:
    print('O jogador  escolheu papel'.format(player1))
elif player1 == 3:
    print('O jogador  escolheu tesoura'.format(player1))

if player2pc == 1:
    print('O computador escolheu pedra'.format(player2pc))
elif player2pc == 2:
    print('O computador escolheu papel'.format(player2pc))
elif player2pc == 3:
    print('O computador escolheu tesoura'.format(player2pc))
print('======================================')

#empate

if player1 == player2pc:
    print('O jogo deu \033[33mEMPATE\033[m')

#player 1 ganhar
elif (player1 == 1 and player2pc == 3) or (player1 == 2 and player2pc == 1) or (player1 == 3 and player2pc == 2) :
    print('O jogador \033[32mGANHOU\033[m')
else:
    print('O computador \033[31mGANHOU\033[m')
