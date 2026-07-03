print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

matriz = []
soma_pares = 0

for linha in range(3):
    dados = []

    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        dados.append(valor)

        if valor % 2 == 0:
            soma_pares += valor

    matriz.append(dados)

print('-=-' * 12)
print(' MATRIZ DIGITADA '.center(35, ' '))
print('-=-' * 12)

for linha in matriz:
    for valor in linha:
        print(f'[ {valor:^5} ]', end=' ')
    print()

print('-=-' * 12)
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma da terceira coluna {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'Maior valor da segunda linha:{max(matriz[1])}')