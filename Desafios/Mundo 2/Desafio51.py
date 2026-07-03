print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('Bem vindo ao Desafio 51 (PA)')
print('=' * 20)
print('Para continuar, digite')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

print('=' * 20)
print('Os 10 termos da PA são: ',end = '')

for c in range(1, 11):
    x = primeiro + (c-1)*razao
    print('{}'.format(x), end=' ')