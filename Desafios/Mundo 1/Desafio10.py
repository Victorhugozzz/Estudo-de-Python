print('===== DESAFIO 10 =====')
n1 = float(input('Digite um numero inteiro: '))
n2 = 1
print('A tabuada do numero {} é: '.format(n1))
while n2<=10:
    n3 = n1 * n2
    print('{} X {} = {:.2f}'.format(n1, n2, n3))
    n2+=1

