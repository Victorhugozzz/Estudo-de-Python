print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

campeonato = {
  'nome': str(input('Nome do Jogador: ')),
  'partidas': int(input('Quantas partidas ele jogou: ')),
  'gols': [],
  'total': 0
}

for c in range(campeonato['partidas']):
  campeonato['gols'].append(int(input(f'Quantos gols na partida {c+1}: ')))
  campeonato['total'] += campeonato['gols'][c]

print('-=' * 20)
print(campeonato)
print('-=' * 20)

print(f'O jogador {campeonato["nome"]} jogou {campeonato["partidas"]} partidas.')

for c in range(campeonato['partidas']):
  print(f'   => Na partida {c+1}, fez {campeonato["gols"][c]} gols.')

print(f'Foi um total de {campeonato["total"]} gols.')