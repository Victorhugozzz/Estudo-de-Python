import math
print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)
tot = 0
num = int(input('Digite um numero para testar se é primo: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print(f'O numero {num} é primo: SIM')
else:
    print(f'O numero {num} é primo: NÃO')