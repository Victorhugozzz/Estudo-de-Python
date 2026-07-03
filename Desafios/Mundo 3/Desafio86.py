print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

matriz1 = []
matriz2 = []
matriz3 = []
dados = []

for c in range (0, 3):
  a = int(input(f'Digite um valor inteiro [0, {c}]: '))
  dados.append(a)
  matriz1.append(dados[:])
  dados.clear()

for c in range (0, 3):
  b = int(input(f'Digite um valor inteiro [1, {c}]: '))
  dados.append(b)
  matriz2.append(dados[:])
  dados.clear()

for c in range (0, 3):
  c = int(input(f'Digite um valor inteiro [2, {c}]: '))
  dados.append(c)
  matriz3.append(dados[:])
  dados.clear()


print('-=-' * 12)
print('As matrizes digitadas foram'.center(40, " "))
print('-=-' * 12)

for valor in matriz1:
  print(f'[ {valor[0]:^5} ]', end=' ')
print()

for valor in matriz2:
  print(f'[ {valor[0]:^5} ]', end=' ')
print()

for valor in matriz3:
  print(f'[ {valor[0]:^5} ]', end=' ')
print()