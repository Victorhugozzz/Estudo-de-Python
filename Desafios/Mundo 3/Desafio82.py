print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

lista = []
pares = []
impares = []
opcao = ''

while opcao !='N':
  a = int(input('Digite um valor inteiro: '))
  lista.append(a)

  if a % 2 == 0:
    pares.append(a)
  else:
    impares.append(a)

  opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

  if opcao not in 'SN':
    print('Opção inválida !')
    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

print('-=-' * 16)
print('Os valores digitados foram {}'.format(sorted(lista)))
print('Os valores digitados que sao pares foram {}'.format(sorted(pares)))
print('Os valores digitados que sao impares foram {}'.format(sorted(impares)))
print('-=-' * 16)