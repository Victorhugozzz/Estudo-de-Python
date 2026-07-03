print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

lista = []

a = str (input('Digite uma expressao: '))
lista.append(a)

if a.count('(') == a.count(')'):
  print('Sua expressao esta correta !')
else:
  print('Sua expressao esta errada !')
