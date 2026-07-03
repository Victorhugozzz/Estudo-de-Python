print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

valores = []
opcao = ''
while opcao != 'N':
  a = int(input('Digite um valor inteiro: '))
  if a not in valores:
    valores.append(a)
    valores.sort()
    print('Valor adicionado com sucesso !')
  else:
    print('Valor duplicado ! , nao vou adicionar')
  opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

print('-=-' * 26)
print('Os valores digitados foram {}'.format(valores))
print('-=-' * 26)