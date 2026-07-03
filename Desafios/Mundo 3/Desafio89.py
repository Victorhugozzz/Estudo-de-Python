
print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30))
print('=' * 20)

boletim = []
opcao = ''

while opcao != 'N':

  nome = (str(input('Digite o nome do aluno: ')))
  nota1 = (float(input('Digite a primeira nota do aluno: ')))
  nota2 = (float(input('Digite a segunda nota do aluno: ')))
  media = (nota1 + nota2) / 2
  
  boletim.append([nome, nota1, nota2, media])

  opcao = str(input('Quer continuar ? [S/N]')).upper().strip()

  if opcao not in 'SN':
    print('Opção inválida !')
    opcao = str(input('Quer continuar ? [S/N]')).upper().strip()
    

print('-=-' * 20)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
for i in range(0, len(boletim)):
  print(f'{i:<4}{boletim[i][0]:<10}{boletim[i][3]:>8.1f}')
print('-' * 30)

while True:
  opcao = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
  if opcao == 999:
    break
  else:
    print(f'As notas do aluno {boletim[opcao][0]} foram: \nNOTA 1 = {boletim[opcao][1]} \nNOTA 2 = {boletim[opcao][2]} \nA media ficou em {boletim[opcao][3]:.1f}')
    print('-' *   30)