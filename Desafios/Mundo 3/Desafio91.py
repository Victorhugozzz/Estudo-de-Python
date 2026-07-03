import random
import time

print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)
dados = {}
ranking = []
print('VAMOS JOGAR DADOS !')
opcao = input('Quer jogar ? [S/N] ').upper().strip()

while opcao not in 'SN':
  print('Opção inválida !')
  opcao = input('Quer jogar ? [S/N] ').upper().strip()

if opcao == 'S':
  print('Vamos jogar !')
  time.sleep(0.5)
  
  print('Sorteando os dados...')
  time.sleep(1)
  
  for n in range(1, 5):
    valor = random.randint(1, 6)
    dados[f'Jogador {n}'] = valor
    
    print(f'Jogador {n} tirou {valor} no dado.')
    time.sleep(0.5)
    
    ranking= list(dados.items())
    ranking.sort(key=lambda item: item[1], reverse=True)
   
  print() 
  print('=-=' * 20)
  print('O JOGO ACABOU ! \nOs vencedores foram os jogadores: ')
  for posicao, jogador in enumerate(ranking):
    print(f'{posicao + 1}o lugar: {jogador[0]} com {jogador[1]} .')
  print('=-=' * 30)
