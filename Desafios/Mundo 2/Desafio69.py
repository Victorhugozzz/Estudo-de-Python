print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

mulheres_menor_de20 = 0
homens = 0
maior = 0
opcao = ''
while opcao != 'N':
  idade = int(input('Digite um idade: '))
  if idade > 18:
    maior += 1
  sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres_menor_de20 += 1
  opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
  if opcao == 'N':
    print('=' * 30)
    print('Dos dados cadastrados foram:')
    print(f'{maior} pessoas maiores de idade\n{homens} homens\n{mulheres_menor_de20} mulheres tem menos de 20 anos')
    break