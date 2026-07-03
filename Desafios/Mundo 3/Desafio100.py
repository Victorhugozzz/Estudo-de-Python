import random
import time
print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)
numeros = []
def sorteio():
    for c in range(5):
        n = random.randint(1, 9)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
    print(' Pronto!')
    print('Analisando valores aleatorios...')
    time.sleep(1)
def somaPares():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'\nA soma dos valores pares é: {soma}')
    
sorteio()
somaPares()