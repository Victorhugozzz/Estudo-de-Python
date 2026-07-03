print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

print('Bem vindo ao Desafio 61 (PA)')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print('=' * 20)
print('Os 10 termos da PA são:')

c = 1

while c <= 10:
    termo = primeiro + (c - 1) * razao
    print(termo, end=' ')
    c += 1