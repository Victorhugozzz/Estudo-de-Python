print('=' * 20)
print('\033[31m      DESAFIO\033[m')
print('=' * 20)

n1 = float(input('Digite um numero inteiro: '))
n2 = 1
print('A tabuada do numero {} é: '.format(n1))
for n2 in range(1, 11):
    n3 = n1 * n2
    print('{} X {} = {:.2f}'.format(n1, n2, n3))
    n2+=1
