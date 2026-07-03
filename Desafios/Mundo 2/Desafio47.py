print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

for c in range(1,51):
    if c % 2 == 0:
        print(f'\033[36m{c}\033[m', end=' ')
