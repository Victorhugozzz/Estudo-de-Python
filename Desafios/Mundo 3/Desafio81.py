print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

lista = []
opcao = ''

while opcao != 'N':
  a = int(input('Digite um valor inteiro: '))
  print('Valor adicionado com sucesso !')
  lista.append (a)
  opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()

  if opcao not in 'SN':
    print('Opção inválida !')
    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()
    
print('-=-' * 26)
print('Os valores digitados foram {}'.format(lista))
print('A quantidade de valores digitados foi {}'.format(len(lista)))
print('A lista em ordem decrescente fica {}'.format(sorted(lista, reverse=True)))
print('O valor 5 faz parte da lista' if 5 in lista else 'O valor 5 nao faz parte da lista')
print('-=-' * 26) 


  