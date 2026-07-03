
pessoas = list()
dados = list()
opcao = ''
while opcao != 'N':
  dados.append(str(input('Digite o nome da pessoa: ')))
  dados.append(int(input('Digite o peso desta pessoa: ')))
  pessoas.append(dados[:])
  dados.clear()

  opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

  if opcao not in 'SN':
    print('Opção inválida !')
    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()
  elif opcao == 'N':
    
    break

print('-=-' * 20)
print(f'O total de pessoas cadastradas foi {len(pessoas)}')

maior_peso = pessoas[0][1]

for p in pessoas:
  if p[1] > maior_peso:
    maior_peso = p[1]

print(f'Maior peso foi {maior_peso} kg. Peso de:', end=' ')

for p in pessoas:
  if p[1] == maior_peso:
    print(f'{p[0]}')

menor_peso = pessoas[0][1]

for p in pessoas:
  if p[1] < menor_peso:
    menor_peso = p[1]

print(f'Menor peso foi {menor_peso} kg. Peso de :', end=' ')

for p in pessoas:
  if p[1] == menor_peso:
    print(f'{p[0]}')