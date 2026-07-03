print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

valores = []

for c in range(0,5):
  a = int(input('Digite um valor inteiro: '))
  valores.append(a)

print('=' * 40)
print(f'O maior valor digitado foi {max(valores)} na posicao {valores.index(max(valores))+ 1} !')
print(f'O maior valor digitado foi {min(valores)} na posicao {valores.index(min(valores))+ 1} !')
print('=' * 40)