print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

print('Bem vindo ao Desafio 61 (PA)')
print('=' * 30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
quantidade = int(input('Quantidade de termos na PA: '))

print('=' * 30)

print(f'Os {quantidade} primeiros termos da PA são: ',end = '')

for c in range(1, quantidade + 1):
    x = primeiro + (c-1)*razao
    print('{}'.format(x), end=' ')