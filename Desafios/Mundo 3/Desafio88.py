import random
import time

print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

valores = []

chutes = int(input('Quantos jogos você quer que sejam sorteados? '))

for c in range(chutes):

    dados = []
    
    while len(dados) < 6:

        n = random.randint(1, 60)

        if n not in dados:
            dados.append(n)

    dados.sort()

    valores.append(dados[:])

    print('-' * 30)
    print(f'Jogo {c + 1}: {valores[c]}')

    time.sleep(1)

print('\n',' <- BOA SORTE -> '.center(30, '-'))

