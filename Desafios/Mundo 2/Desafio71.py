print('=' * 20)
print('\033[31m> BANCO DO BRASIL\033[m')
print('=' * 20)

valor = int(input('Qual o valor que deseja sacar? R$'))

total50 = 0
total20 = 0
total10 = 0
total1 = 0

while True:
  if valor >= 50:
    valor -= 50
    total50 += 1

  elif valor >= 20:
    valor -= 20
    total20 += 1

  elif valor >= 10:
    valor -=10
    total10 += 1

  elif valor >= 1:
    valor -= 1
    total1 += 1
  else:
    break
      
print (f'Total de {total50} cedulas de R$50')
print (f'Total de {total20} cedulas de R$20')
print (f'Total de {total10} cedulas de R$10')
print (f'Total de {total1} cedulas de R$1')
