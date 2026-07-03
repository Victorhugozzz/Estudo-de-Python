import time

print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

num = int(input('Digite um numero para ver seu fatorial: '))
fatorial = 1
for c in range(1, num + 1):
    fatorial = c * fatorial
print(f'{num}! = {fatorial}', end=' ')