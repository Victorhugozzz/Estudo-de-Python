n1 = int(input('Digite um numero 1: '))
n2 = int(input ('Digite um numero 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n'
      'O produto é {},\n'
      'A divisão é {:.3f}\n'.format(s, m, d))
print('A divisão inteira é {},\n'
      'A potência é {}'.format(di, e))