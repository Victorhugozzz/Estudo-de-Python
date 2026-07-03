import random

print('===== \033[31mDESAFIO 29\033[m =====')
numpla = int(input('Digite um numero de 1 a 5 e tente a sua sorte: '))
num = int(random.randint(1, 5))
if numpla == num:
    print('\033[1;32mVoce acertou\033[m, parabens!!!')
else:
    print('\033[1;31mVoce errou\033[m, o numero era {}, tente novamente '.format(num))