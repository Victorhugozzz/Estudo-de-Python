import random

print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

num = 0
num2 = 1
tentativas = 0
while num != num2:
    num = int(input('Digite um numero e tente a sua sorte: '))
    num2 = random.randint(1,10)
    print('\033[1;31mVoce errou\033[m, o numero era {}, tente novamente '.format(num))
    tentativas += 1
if num == num2:
    print(f'\n\033[1;32mVoce acertou\033[m, parabens o numero era {num} e foram necessarias {tentativas} tentativas!!!')