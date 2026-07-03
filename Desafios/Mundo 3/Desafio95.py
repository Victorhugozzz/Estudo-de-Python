print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

opcao = ''
jogos = list()

while opcao != 'N':
    campeonato = {
        'nome': str(input('Nome do Jogador: ')),
        'partidas': int(input('Quantas partidas ele jogou: ')),
        'gols': [],
        'total': 0
    }

    for c in range(campeonato['partidas']):
        campeonato['gols'].append(
            int(input(f'Quantos gols na partida {c + 1}: '))
        )
        campeonato['total'] += campeonato['gols'][c]

    jogos.append(campeonato.copy())

    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()
    print('-' * 50)

    while opcao not in 'SN':
        print('Opção inválida!')
        opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

print('-=' * 20)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<20}{"Total"}')
print('-' * 50)

for c, jogador in enumerate(jogos):
    print(
        f'{c:<5}'
        f'{jogador["nome"]:<15}'
        f'{str(jogador["gols"]):<20}'
        f'{jogador["total"]}'
    )

print('-' * 50)

while True:
    teste = input('Mostrar dados de qual jogador? (999 para parar) ')

    if not teste.isnumeric():
        print('Digite apenas números!')
        continue

    teste = int(teste)

    if teste == 999:
        break

    if teste >= len(jogos) or teste < 0:
        print('Código inexistente!')
        continue

    print('-' * 30)
    print(f'LEVANTAMENTO DO JOGADOR {jogos[teste]["nome"]}')
    print('-' * 30)

    for i, gols in enumerate(jogos[teste]["gols"]):
        print(f'  No jogo {i + 1}: {gols} gol(s)')

    print('-' * 30)