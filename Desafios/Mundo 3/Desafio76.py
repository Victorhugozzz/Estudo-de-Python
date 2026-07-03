print('-'*43)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*43)

listagem = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

for i,c in enumerate(listagem, start= -1):
    print('R$ {:<30}'.format(c), end=' ')

    if i % 2 == 0:
        print()
print('-'*43)