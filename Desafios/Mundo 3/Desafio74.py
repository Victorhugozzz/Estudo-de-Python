import random
print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

lista = (random.randint(1,10),
         random.randint(1,10),
         random.randint(1,10),
         random.randint(1,10),
         random.randint(1,10))


print(f'Os valores sorteados foram: {lista}')
print(f'MENOR VALOR: {min(lista)}')
print(f'MAIOR VALOR: {max(lista)}')
