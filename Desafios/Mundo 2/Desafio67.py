print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)
while True:
  print('-' * 40)
  num = int(input('Digite um numero para ver sua tabuada: '))
  if num < 0 :
    break
  else:
    for c in range(1, 11):
      print(f'{num} x {c} = {num * c}')
      
print('=' * 40)
print('PROGRAM TABUADA ENCERRADO. Volte sempre!')