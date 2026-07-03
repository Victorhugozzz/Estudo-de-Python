print('=' * 20)
print('\033[31mDESAFIO\033[m'.center(30, " "))
print('=' * 20)

valores = []
total9 = 0
pares = []

for c in range(0, 4):
    a = int(input('Digite um valor inteiro: '))
    valores.append(a)

tupla = tuple(valores)

print(f'Os numero digitados foram {tupla} !')
print(f'O numero 9 apareceu {tupla.count(9)} vez(s) !')

if 3 in tupla:
    print('O numero 3 apareceu na posição {}'.format(tupla.index(3) + 1))
else:
    print('O numero 3 nao foi digitado na lista')

pares = [n for n in tupla if n % 2 == 0]
print(f'Os numeros pares digitados foram {pares} !')