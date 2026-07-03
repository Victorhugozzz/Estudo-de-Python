print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)


total = 0
produto_mil = 0
nome_barato = ''
menor = 0
contador = 0

print('Bem vindo a \033[33mCALCULADORA\033[m de produtos')

while True:
  nome = str(input('Digite o nome do produto: '))
  preco = float(input('Digite o preco do produto: '))

  total += preco

  if preco > 1000:
    produto_mil += 1

  contador += 1

  if contador == 1 or preco < menor:
    menor = preco
    nome_barato = nome

  opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

  while opcao not in ['S', 'N']:
    opcao = str(input('Opcao invalida. Digite? [S/N] ')).strip().upper()
  if opcao == 'N':
    break
print('-' * 30)
print('Resumo das compras')
print(f'Total gasto na compra: R${total:.2f}')
print(f'Tem {produto_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${menor:.2f}')
print('-' * 30)

    