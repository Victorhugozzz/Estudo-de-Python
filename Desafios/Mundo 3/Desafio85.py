print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

valores = list()
par = list()
impar = list()
dados = list()
for c in range (0, 7):
  a = int(input('Digite um valor inteiro: '))
  if a % 2 == 0:
    par.append(a)
  else:
    impar.append(a)
  dados.append(a)
  valores.append(dados[:])
  dados.clear()

print('-=-' * 20)
print(f'Os valores digitados foram {sorted(valores)}')
print(f'Os valores pares digitados foram {sorted(par)}')
print(f'Os valores impares digitados foram {sorted(impar)}')
print('-=-' * 20)